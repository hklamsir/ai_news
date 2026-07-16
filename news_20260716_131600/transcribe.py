from faster_whisper import WhisperModel
import os

work_dir = "/home/lamsir/ai_news/news_20260716_131600"
audio_path = os.path.join(work_dir, "audio_16k.wav")
print(f"開始轉錄（tiny 模型）：{audio_path}")
print(f"檔案存在：{os.path.exists(audio_path)}")

model = WhisperModel('tiny', device='cpu', compute_type='int8')
print("模型載入完成")
segments, info = model.transcribe(audio_path, language='zh')

print(f"語言：{info.language}，持續時間：{info.duration}s")

transcript = []
for s in segments:
    transcript.append(s.text)

result = '\n'.join(transcript)
print(f"轉錄完成，共 {len(transcript)} 段")

# 寫入 transcript.txt
with open(os.path.join(work_dir, 'transcript.txt'), 'w', encoding='utf-8') as f:
    f.write(result)
print(f"已寫入 transcript.txt")

# 同時寫入 title.txt
with open(os.path.join(work_dir, 'title.txt'), 'w', encoding='utf-8') as f:
    f.write("Anthropic 最新論文解析：Claude 大腦裡的全域工作間")
print(f"已寫入 title.txt")
