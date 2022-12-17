# Image Processing (Template)
Python으로 구현된 이미지 프로세싱 강의용 소스코드입니다. 
이 프로그램은 Histogram equalizer, Thresholding, Transformation 등 다양한 이미지 처리 기법들을 구현하고 쉽게 기능으로 추가할 수 있는 템플릿입니다.

## Requirements
Python의 pip를 이용해 아래 의존성을 설치합니다.
```text
- PyQt5
- numpy
- opencv-python
- qimage2ndarray
```

## Implementation
소스코드 중 `IpImageProcess.py`에 이미지 처리를 수행할 몇 가지 함수들이 준비되어 있습니다 (예: `set_threshold`).
이 함수들을 구현하면 쉽게 이미지 처리 프로그램을 완성할 수 있습니다.
`IpImageProcess.py`에 준비된 함수 이외에 새로운 이미지 처리 기법을 구현하고 싶다면, 
`IpMenubar.py`에서 새로운 메뉴와 액션을 추가하고, 콜백 함수를 연동하십시오. 