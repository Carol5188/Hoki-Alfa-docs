# YouTube 一起看 · 中英阿文案候选

v2.0｜2026-10-23｜阿语待母语审校；用于产品/开发评审，不代表已翻译上线。

稳定前缀 `room_watch.`。原型字典使用短 key，接入时按下表映射；现有房间设置、麦克风、公屏、发送、关闭等复用原项目 key。普通确认按钮按系统语义布局，不依赖视觉左右顺序；URL、video_id与时间采用 LTR 隔离。标题取官方资料，不翻译或修改官方视频名。

| key 后缀 | 展示/触发 | 中文 | English | العربية |
|---|---|---|---|---|
| entry | 工具/有资格房间的房主与管理员 | YouTube 一起看 | Watch YouTube Together | المشاهدة معًا · YouTube |
| select_title | 首次选片 | 选择 YouTube 视频 | Choose a YouTube video | اختر فيديو من YouTube |
| link_label | 链接表单 | YouTube 视频链接 | YouTube video link | رابط فيديو YouTube |
| link_hint | 链接表单 | 粘贴一个视频链接，先预览，再邀请大家一起看。 | Paste a video link, preview it, then invite everyone to watch. | ألصق رابط فيديو، واعرض المعاينة، ثم ابدأ المشاهدة مع الجميع. |
| preview | 按钮 | 预览视频 | Preview video | معاينة الفيديو |
| preview_loading | 请求中 | 正在获取视频… | Loading video… | جارٍ تحميل الفيديو… |
| preview_ready | 预览成功 | 已获取视频预览 | Video preview ready | معاينة الفيديو جاهزة |
| preview_note | 预览下方 | 预览仅验证当前可播放性，成员地区与账号可能影响播放。 | Availability may vary by region and account. | قد تختلف إمكانية التشغيل حسب المنطقة والحساب. |
| start | 确认发起按钮 | 开始一起看 | Start watching together | ابدأ المشاهدة معًا |
| invited | 发起成功 | 已邀请房间成员一起看 | Room members have been invited | تمت دعوة أعضاء الغرفة |
| invite_title | 未加入卡 | 邀请你一起看 | You are invited to watch together | 待按v2.0角色规则审校 |
| join | 未加入按钮 | 加入观看 | Join watching | انضم للمشاهدة |
| rejoin | 收起后按钮 | 重新加入 | Rejoin | انضم مجددًا |
| autoplay_title | 播放被拦截 | 点一下，跟上大家 | Tap to watch with everyone | انضم للحظة الحالية |
| autoplay_hint | 被拦截说明 | 需要你手动开启本机播放 | Tap to start playback on your device | اضغط لبدء التشغيل على جهازك |
| autoplay_play | 手势兜底按钮 | 点击播放 | Tap to play | تشغيل الفيديو |
| shared_pause | 管理者按钮 | 全房暂停 | Pause for everyone | إيقاف للجميع |
| shared_play | 管理者按钮 | 全房播放 | Play for everyone | تشغيل للجميع |
| host_control_hint | 卡片外提示 | 房主与管理员控制共享播放 | The host and room admins control shared playback | 待按v2.0角色规则审校 |
| personal_audio_hint | 卡片外提示 | 音量仅对自己生效 | Volume affects only you | الصوت على جهازك فقط |
| mute | 本机按钮 | 静音 | Mute | كتم |
| unmute | 本机按钮 | 开声音 | Unmute | تفعيل الصوت |
| volume | 本机设置 | 视频音量 | Video volume | صوت الفيديو |
| enlarge | 本机按钮 | 放大 | Expand | تكبير |
| back_to_room | 放大状态返回 | 返回房间 | Back to room | العودة للغرفة |
| hide | 收起按钮 | 收起 | Hide | إخفاء |
| hidden_hint | 收起后卡片 | 已停止本机观看 | Playback stopped on your device | توقفت المشاهدة على جهازك |
| resync | 本机未同步/恢复 | 跟上当前进度 | Sync with the room | مزامنة مع الغرفة |
| replace_title | 管理者换片 | 更换视频 | Change video | تغيير الفيديو |
| replace_confirm | 确认换片 | 确认更换 | Confirm change | تأكيد التغيير |
| end_title | 管理者结束确认标题 | 结束全房一起看？ | End watching for everyone? | إنهاء المشاهدة للجميع؟ |
| end_body | 确认正文 | 视频会对所有成员停止播放。你们仍然留在语聊房中。 | The video will stop for everyone. You will all stay in the voice room. | سيتوقف الفيديو للجميع، وستبقون في الغرفة الصوتية. |
| end_confirm | 确认按钮 | 结束一起看 | End watching together | إنهاء المشاهدة |
| keep_watching | 取消结束 | 继续观看 | Keep watching | متابعة المشاهدة |
| ended | 房间结束提示 | 一起看已结束 | Watching together has ended | انتهت المشاهدة معًا |
| media_ended | 自然结束 | 视频已播完，等待管理者换片 | The video has ended. Waiting for a host or admin. | 待按v2.0角色规则审校 |
| invalid_link | 格式不通过 | 请输入有效的 YouTube 单视频链接 | Enter a valid YouTube video link | أدخل رابط فيديو YouTube صالحًا |
| unsupported_type | Shorts/直播/列表 | 首期支持普通点播视频，暂不支持 Shorts、直播或播放列表 | This version supports regular videos only, without Shorts, live streams or playlists | ندعم الفيديو المسجل فقط، دون البث المباشر أو Shorts أو قوائم التشغيل |
| not_embeddable | 不允许嵌入 | 此视频不允许在房间内播放，请换一个链接 | This video cannot play in the room. Try another link. | لا يمكن تشغيل هذا الفيديو في الغرفة. اختر رابطًا آخر. |
| preview_timeout | 解析超时 | 获取视频超时，请重试 | Loading timed out. Try again. | انتهت مهلة التحميل. حاول مجددًا. |
| local_error_title | 本机播放器失败 | 暂时无法播放 | Playback is temporarily unavailable | تعذّر التشغيل مؤقتًا |
| local_network_hint | 本机网络失败 | 你的网络异常，其他人仍在观看。 | Your connection is unstable. Others are still watching. | اتصالك ضعيف. يواصل الآخرون المشاهدة. |
| host_offline | 无人管理 | 暂无在线管理者，共享播放已暂停 | No host or admin is online. Shared playback is paused. | 待按v2.0角色规则审校 |
| host_timeout | 无人管理超时 | 管理者长时间未连接，一起看已结束 | No host or admin returned. Shared watching has ended. | 待按v2.0角色规则审校 |
| host_left | 房主身份转移 | 房主已变更，本场一起看已结束 | The room owner changed. This session has ended. | 待按v2.0角色规则审校 |
| host_exit_title | 最后管理者离房确认 | 最后一名管理者要离开？ | Is the last host or admin leaving? | 待按v2.0角色规则审校 |
| host_exit_confirm | 确认离房 | 确认离开 | Confirm leaving | 待按v2.0角色规则审校 |
| headphones_hint | 首次观看轻提示 | 建议使用耳机，避免视频声音进入麦克风 | Use headphones to avoid microphone echo | ننصح بسماعات أذن لتجنب الصدى. |
| report_video | 成员菜单 | 举报视频 | Report video | الإبلاغ عن الفيديو |
| bgm_conflict | 有BGM/开始前 | 开始一起看会暂停房间背景音乐。 | Starting will pause the room’s background music. | سيؤدي البدء إلى إيقاف موسيقى الغرفة مؤقتًا. |
| permission_denied | 权限不足 | 仅房主或本房管理员可管理一起看 | Only the host or room admins can manage shared watching | 待按v2.0角色规则审校 |
| newer_version | 旧版本邀请卡 | 升级后加入一起看 | Update the app to join | حدّث التطبيق للانضمام للمشاهدة. |
| start_failed | 发起/换片接口失败 | 操作未完成，请重试 | The action could not be completed. Try again. | تعذّر إكمال العملية. حاول مجددًا. |
| region_restricted | 区域不可播放 | 此视频在你所在地区不可播放 | This video is unavailable in your region | هذا الفيديو غير متاح في منطقتك. |
| private_or_removed | 视频无效 | 视频不可用，可能已删除或设为私密 | The video is unavailable. It may be private or removed. | الفيديو غير متاح. ربما حُذف أو أصبح خاصًا. |
| login_restricted | 需年龄/账号验证 | 此视频需要在 YouTube 完成验证，暂不能在房内播放 | This video requires verification on YouTube and cannot play in the room | يتطلب الفيديو التحقق على YouTube ولا يمكن تشغيله في الغرفة. |
| feature_disabled | 紧急关停 | 一起看暂不可用，你可以继续语聊 | Shared watching is unavailable. You can continue chatting. | المشاهدة معًا غير متاحة. يمكنك متابعة الدردشة الصوتية. |

按钮「取消/关闭/重试」、房间退出/模式切换确认沿用现有 key；涉及本场一起看的影响说明须引用本表。新片标题、可播放性原因、人数与时长为参数，不写死；人数标注为本房 Hoki 参与者，不是 YouTube 全站观看量。

本表补全了方案中尚未接入原型的 BGM、版本、权限、真实服务失败和地区/账号错误文案。原型的举报完成、退出导航等明确注明演示，不复用为正式成功回执。仅语聊房内容分享，无余额不足、扣费、返奖等新文案。

## v2.0新增文案

稳定前缀仍为room_watch。角色/生命周期变更行的阿语单列待审校，不沿用已失效的仅房主语义。后台本轮为中文运营界面，其他语言未制作。

| key后缀 | 触发 | 中文 | English | 阿语 |
|---|---|---|---|---|
| room_ineligible | 资格收回 | 房间暂不具备一起看资格 | Shared watching is unavailable in this room | 待审校 |
| permission_changed | 角色/版本失效 | 操作权限已变化，请重新进入 | Your permissions changed. Reopen this feature. | 待审校 |
| no_controller_leave_body | 最后一名管理者离房 | 离开后共享播放将暂停，等待管理者返回；超时后结束。 | Shared playback will pause until a host or admin returns, then end if the wait expires. | 待审校 |
| controller_returned | 管理者返回 | 管理者已返回，可继续播放 | A host or admin returned. Playback can resume. | 待审校 |

后台新增固定文案：房主白名单、继承统一默认门槛、单独设置最低财富等级、不限财富等级（白名单豁免）、有效/停用/过期/财富未达标、操作原因、保存失败/版本冲突。后台明确展示原因，不复用客户端无权限Toast掩盖配置错误。

旧host_offline/host_timeout等key为兼容命名，触发条件已改为无有效在线管理者；host_left改用于身份转移，单纯房主离线且有管理员在时不触发。正式接入可迁移到controller前缀并处理旧客户端。
