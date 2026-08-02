import os
import google.generativeai as genai
from PIL import Image

def generate_video_prompt():
    # 1. API 키 설정
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("에러: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
        return

    genai.configure(api_key=api_key)

    # 2. 이미지 로드
    try:
        image = Image.open("input_image.png")
    except FileNotFoundError:
        print("에러: 'input_image.png' 파일을 찾을 수 없습니다. 현재 디렉토리에 파일을 준비해주세요.")
        return
    except Exception as e:
        print(f"이미지 로드 중 오류 발생: {e}")
        return

    # 3. 사용자 텍스트 프롬프트 입력
    user_prompt = input("비디오 생성에 사용할 텍스트 프롬프트를 입력하세요: ")

    # 4. 모델 설정 및 콘텐츠 생성
    # gemini-1.5-flash 모델 사용
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 프롬프트 엔지니어링: 역할을 부여하고 기대하는 출력 형식을 명확히 함
    system_instruction = """
    당신은 전문적인 비디오 생성 프롬프트 엔지니어입니다.
    사용자가 제공한 이미지와 텍스트 프롬프트를 바탕으로, AI 비디오 생성 모델(예: Sora, Runway Gen-2, Pika 등)에 사용할 수 있는 매우 상세하고 생생한 비디오 모션 프롬프트를 영어로 작성해주세요.
    카메라 워크, 피사체의 움직임, 조명 변화, 분위기 등을 구체적으로 묘사해야 합니다.
    """

    prompt = [
        system_instruction,
        "사용자 텍스트 프롬프트: " + user_prompt,
        image
    ]

    try:
        print("\n비디오 모션 프롬프트를 생성 중입니다...\n")
        response = model.generate_content(prompt)
        print("=== 생성된 비디오 모션 프롬프트 ===")
        print(response.text)
        print("===================================")
    except Exception as e:
        print(f"콘텐츠 생성 중 오류 발생: {e}")

if __name__ == "__main__":
    generate_video_prompt()
