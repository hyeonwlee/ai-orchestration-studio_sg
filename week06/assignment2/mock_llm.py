import random

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    is_faulty = random.choice([1, 0, 0, 0, 0])
    if is_faulty: fault_type = random.choice(["code_fence", "extra_text", "truncated"])

    reviews_keywords = {
        "배송": '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불": '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질": '{"category": "품질", "sentiment": "긍정", "score": 5}',
    }

    for keyword, canned in reviews_keywords.items():
        if keyword in user_message: 
            response_text = canned
            break
        else: response_text = '{"category": "기타", "sentiment": "중립", "score": 3}'

    if is_faulty:
        if fault_type == "code_fence":
            response_text = "```json\n" + response_text + "\n```"
        elif fault_type == "extra_text":
            response_text = "물론입니다! 분석 결과는 다음과 같습니다. " + response_text
        else:
            response_text = response_text[:26]

    return {"text": response_text, 
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 120, "output_tokens": 35}}