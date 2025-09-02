# [FastAPI](https://fastapi.tiangolo.com/ko/)
- Vast, API
[Github](https://github.com/fastapi/fastapi)

Key Notes
- Easy, Quick
- Robust
- Standards

CLI
- [Typer](https://typer.tiangolo.com/)


Add
- 웹 부분을 위한 Starlette.[Starlette])(https://www.starlette.io/)
- 데이터 부분을 위한 Pydantic.[pydantic](https://docs.pydantic.dev/latest/#pydantic-examples)


uvicorn : 프로덕션을 위한 ASGI 서버
(ASGI server, such as uvicorn, daphne, or hypercorn.)
```bash
pip install fastapi
pip instatll "uvicorn[standard]" 
```

```bash
uvicorn main:app --reload
````
기본 : 8000
swagger 자동 생성: docs
swagger 수정 : redoc

```python
item_id : int

item : Item
```

선언을 하면
```plain text
다음을 포함한 편집기 지원:
- 자동완성.
- 타입 검사.

데이터 검증:
- 데이터가 유효하지 않을 때 자동으로 생성하는 명확한 에러.
- 중첩된 JSON 객체에 대한 유효성 검사.

입력 데이터 변환: 네트워크에서 파이썬 데이터 및 타입으로 전송. 읽을 수 있는 것들:
- JSON.
- 경로 매개변수.`
- 쿼리 매개변수.
- 쿠키.
- 헤더.
- 폼(Forms).
- 파일.

출력 데이터 변환: 파이썬 데이터 및 타입을 네트워크 데이터로 전환(JSON 형식으로):
- 파이썬 타입 변환 (str, int, float, bool, list, 등).
- datetime 객체.
- UUID 객체.
- 데이터베이스 모델.
...더 많은 것들.

대안가능한 사용자 인터페이스를 2개 포함한 자동 대화형 API 문서:
- Swagger UI.
- ReDoc.
```


### Todo List for Using FastAPI 
- 서로 다른 장소에서 매개변수 선언: 헤더, 쿠키, 폼 필드 그리고 파일.
- maximum_length 또는 regex처럼 유효성 제약하는 방법.
- 강력하고 사용하기 쉬운 의존성 주입 시스템.
- OAuth2 지원을 포함한 JWT tokens 및 HTTP Basic을 갖는 보안과 인증.
- (Pydantic 덕분에) 깊은 중첩 JSON 모델을 선언하는데 더 진보한 (하지만 마찬가지로 쉬운) 기술.
- (Starlette 덕분에) 많은 추가 기능:
- 웹 소켓
- GraphQL
- HTTPX 및 pytest에 기반한 극히 쉬운 테스트
- CORS
- 쿠키 세션


pip install fastapi[all]를 통해 이 모두를 설치

선택가능한 의존성¶
- Pydantic이 사용하는:
  - email-validator - 이메일 유효성 검사.
- Starlette이 사용하는:
  - HTTPX - TestClient를 사용하려면 필요.
  - jinja2 - 기본 템플릿 설정을 사용하려면 필요.
  - python-multipart - request.form()과 함께 "parsing"의 지원을 원하면 필요.
  - itsdangerous - SessionMiddleware 지원을 위해 필요.
  - pyyaml - Starlette의 SchemaGenerator 지원을 위해 필요 (FastAPI와 쓸때는 필요 없을 것입니다).
  - graphene - GraphQLApp 지원을 위해 필요.
- FastAPI / Starlette이 사용하는:
  - uvicorn - 애플리케이션을 로드하고 제공하는 서버.
  - orjson - ORJSONResponse을 사용하려면 필요.
  - ujson - UJSONResponse를 사용하려면 필요.
