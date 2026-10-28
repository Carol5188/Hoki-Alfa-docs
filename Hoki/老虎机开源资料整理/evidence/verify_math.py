#!/usr/bin/env python3
"""复算文章数字与数学方法；不是原作者Slots实现，不验证S2的96.2%。

运行：python3 verify_math.py
仅依赖Python标准库，输出同目录的数学复算结果.json。
"""
import hashlib
import itertools
import json
import math
import random
from collections import Counter
from datetime import datetime, timezone, timedelta
from fractions import Fraction
from pathlib import Path


def loss_run_dp(hit_rate, run_length, spins):
    alive = [Fraction(0) for _ in range(run_length)]
    alive[0] = Fraction(1)
    for _ in range(spins):
        nxt = [Fraction(0) for _ in range(run_length)]
        nxt[0] = hit_rate * sum(alive)
        for j in range(run_length - 1):
            nxt[j + 1] = (1 - hit_rate) * alive[j]
        alive = nxt
    return 1 - sum(alive)


def toy_payout(symbols):
    # 教学自造配置：3轴，每轴5格，单线下注=总下注=1。
    # Wild可替代A/B；每条线只支付最高有效组合。
    pays = {'A': 1, 'B': 2, 'W': 3}
    candidates = []
    for target, amount in pays.items():
        if target == 'W':
            matches = all(s == 'W' for s in symbols)
        else:
            matches = all(s in (target, 'W') for s in symbols)
        if matches:
            candidates.append(amount)
    return max(candidates, default=0)


def main():
    here = Path(__file__).resolve().parent
    column1 = [6.3, 7.8, 9.4, 10.9, 12.5, 12.5, 14.1, 14.1, 10.9, 1.6, 0]
    column2 = [4.7, 6.3, 7.8, 10.9, 12.5, 14.1, 14.1, 15.6, 12.5, 1.6, 0]
    free_column = [9.4, 9.4, 10.9, 10.9, 12.5, 10.9, 10.9, 10.9, 9.4, 4.7, 0]
    tier_p = [Fraction('0.178'), Fraction('0.064'), Fraction('0.019'),
              Fraction('0.005'), Fraction('0.0008'), Fraction('0.0002'),
              Fraction('0.0000008')]
    tier_min = [1, 5, 20, 100, 500, 1000, 5000]
    lower = sum(p * x for p, x in zip(tier_p, tier_min))
    scatter = sum(p * x for p, x in zip(
        [Fraction('0.0095'), Fraction('0.0015'), Fraction('0.0002')], [2, 10, 50]))

    # 对连续3格窗口逐停点计算；只有1个Scatter，余63格普通符号。
    scatter_strip = ['S'] + ['A'] * 63
    scatter_window = Fraction(sum(
        any(scatter_strip[(stop + offset) % 64] == 'S' for offset in (-1, 0, 1))
        for stop in range(64)), 64)
    independent_scatter = 1 - (Fraction(63, 64) ** 3)

    # 精确DP与枚举对照：3转内至少有一次连续2次无支付。
    dp = loss_run_dp(Fraction(1, 2), 2, 3)
    enumerated = Fraction(sum(
        any(seq[j] == 0 and seq[j + 1] == 0 for j in range(2))
        for seq in itertools.product((0, 1), repeat=3)), 8)
    wrong_window_approx = 1 - (1 - Fraction(1, 2) ** 2) ** 2
    assert dp == enumerated == Fraction(3, 8)

    # 独立教学模型：125个停点完整枚举，再做200,000次固定种子模拟。
    strip = ['A', 'A', 'B', 'B', 'W']
    exact_counts = Counter(toy_payout(symbols) for symbols in itertools.product(strip, repeat=3))
    exact_mean = sum(Fraction(pay * count, 125) for pay, count in exact_counts.items())
    exact_second = sum(Fraction(pay * pay * count, 125) for pay, count in exact_counts.items())
    exact_variance = exact_second - exact_mean ** 2
    assert exact_mean == Fraction(81, 125)
    seed = 20261028
    count = 200_000
    rng = random.Random(seed)  # 仅模拟用，不声称是安全结算RNG。
    sample_counts = Counter()
    batch_results = []
    for batch_size in (12_345, 54_321, 133_334):
        win_sum = 0
        for _ in range(batch_size):
            value = toy_payout([strip[rng.randrange(5)] for _ in range(3)])
            sample_counts[value] += 1
            win_sum += value
        batch_results.append({'rounds': batch_size, 'bet': batch_size, 'win': win_sum,
                              'rtp': win_sum / batch_size})
    observed_count = sum(sample_counts.values())
    assert observed_count == count == sum(b['rounds'] for b in batch_results)
    total_win = sum(pay * freq for pay, freq in sample_counts.items())
    sample_mean = total_win / count
    sample_second_sum = sum(pay * pay * freq for pay, freq in sample_counts.items())
    sample_variance = (sample_second_sum - total_win ** 2 / count) / (count - 1)
    se = math.sqrt(sample_variance / count)
    ci = [sample_mean - 1.96 * se, sample_mean + 1.96 * se]
    merged_mean = sum(b['win'] for b in batch_results) / sum(b['bet'] for b in batch_results)
    assert merged_mean == sample_mean
    assert abs(sample_mean - float(exact_mean)) < 6 * math.sqrt(float(exact_variance) / count)

    results = {
        'scope': '原文算术与数学方法复核；教学模型为独立另造，不是宝藏探险，不是原作者源码验证',
        'generated_at': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_checks': {
            'S2_symbol_column_sums_percent': [round(sum(v), 6) for v in (column1, column2, free_column)],
            'S2_counts_if_nearest_integer_64': [[round(v / 100 * 64) for v in c]
                                              for c in (column1, column2, free_column)],
            'S2_scatter_direct_rtp': float(scatter),
            'S2_tier_probability_sum': float(sum(tier_p)),
            'S2_tier_minimum_rtp_if_total_bet_unconditional_disjoint': float(lower),
            'S2_tier_minimum_rtp_first_four': float(sum(p * x for p, x in zip(tier_p[:4], tier_min[:4]))),
            'S2_tier_minimum_rtp_without_final_subset': float(lower - tier_p[-1] * tier_min[-1]),
            'S2_feature_conditional_ev_total_bet': {'free': .253 / .0112, 'bonus': .052 / .0078},
            'S2_bonus_minimum_ev_if_three_draws_each_minimum_cash_2': 3 * (.75 * 2 + .01 * 100),
            'S2_CV_if_sigma_6_3_mean_0_962': 6.3 / .962,
            'S2_bonus_trigger_lower_bound_if_6_of_64_independent_axes': (6 / 64) ** 2,
            'S2_no_free_trigger_after_100_iid_paid_spins': (1 - .0112) ** 100,
            'S2_no_maxwin_after_one_million_iid_spins': (1 - .0000008) ** 1_000_000,
            'S2_unconditional_percent_100x_plus_among_wins': (.005 + .0008 + .0002 + .0000008) / .267,
            'S2_equal_turnover_lucky_mix_example': .99 * .962 + .01 * 1.02,
            'S3_ten_spin_iid_event_probabilities': [
                {'p': p, 'at_least_one_in_ten': 1 - (1 - p) ** 10, 'mean_wait': 1 / p}
                for p in (.15, .25, .05, .08, .01, .02, .005)],
            'S5_report_total_rtp': 482_450_000_000 / 500_000_000_000,
            'S5_report_sum_components_rtp': sum([.6531, .2177, .0812, .0129]),
            'S5_report_sample_count': 100_000_000_000,
            'S5_rare_event_expected_hits_at_10_billion': 10_000_000_000 / 9_700_000,
            'S5_rare_event_95_relative_halfwidth_at_10_billion': 1.96 * math.sqrt(
                (1 - 1 / 9_700_000) / (10_000_000_000 / 9_700_000)),
        },
        'method_checks': {
            'scatter_reel_window_probability': float(scatter_window),
            'scatter_independent_cell_probability': float(independent_scatter),
            'loss_run_exact_dp': float(dp),
            'loss_run_brute_force': float(enumerated),
            'loss_run_wrong_independent_window_result': float(wrong_window_approx),
            'normal_approx_n_sigma_6_3_95_halfwidth_0_0005': math.ceil((1.96 * 6.3 / .0005) ** 2),
        },
        'teaching_model': {
            'config': {'reels': [strip] * 3, 'rows': 1, 'lines': 1, 'bet': 1,
                       'triple_payouts': {'A': 1, 'B': 2, 'W': 3}, 'wild': 'W',
                       'rule': 'Wild substitutes A/B; pay only maximum valid triple; no features'},
            'exact_outcomes': 125,
            'exact_payout_counts': dict(sorted(exact_counts.items())),
            'exact_rtp': float(exact_mean),
            'exact_hit_rate': 1 - exact_counts[0] / 125,
            'exact_variance': float(exact_variance),
            'simulation_rng': 'Python random.Random / MT; simulation only',
            'simulation_seed': seed,
            'simulation_rounds': count,
            'simulation_payout_counts': dict(sorted(sample_counts.items())),
            'simulation_rtp': sample_mean,
            'simulation_95_ci_normal': ci,
            'exact_value_inside_this_realized_ci': ci[0] <= float(exact_mean) <= ci[1],
            'batch_results': batch_results,
            'merged_rtp': merged_mean,
            'unweighted_batch_rtp_mean_for_comparison': sum(b['rtp'] for b in batch_results) / len(batch_results),
        },
        'assertions_passed': ['loss DP agrees with exact enumeration', 'toy exact mean equals 81/125',
                              'all 200000 planned samples counted', 'sum of batch totals agrees with global totals',
                              'toy sample mean within six exact standard errors of exact value'],
    }
    output = here / '数学复算结果.json'
    output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(output), 'source_minimum_rtp': float(lower),
                      'toy_exact_rtp': float(exact_mean), 'toy_simulated_rtp': sample_mean,
                      'toy_95_ci': ci, 'assertions': len(results['assertions_passed'])}, ensure_ascii=False))


if __name__ == '__main__':
    main()
