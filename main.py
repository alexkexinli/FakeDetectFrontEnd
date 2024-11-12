import gradio as gr
import requests

def upload_and_predict(video):
    if video is None:
        return "请上传一个视频文件。"
    # 将视频文件发送到 FastAPI 接口
    files = {'file': (video.name, video)}
    response = requests.post("http://127.0.0.1:8000/detect", files=files)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"请求失败，状态码：{response.status_code}, 详情：{response.text}"

iface = gr.Interface(
    fn=upload_and_predict,
    inputs=gr.File(label="上传视频文件", type="filepath"),
    outputs="text",
    title="视频人脸检测与推理",
    description="上传一个视频文件，系统将提取包含人脸的帧并进行推理。",
    allow_flagging="never"
)

iface.launch()