* 데이터 손질 과정 설명에 대한 txt 파일입니다. *

1. POSCO DATA를 특정 디렉토리안에 (github의 경우, data_processing 폴더) txt파일로 변환하여 저장합니다. (excute.py 내의 경로만 설정해주면 해당 디렉토리 내에 파일 전체에 있는 txt파일을 모두 읽어 처리합니다.)

2. excute.py로 Data에 대한 filtering을 진행합니다.

	** 원본 데이터에서 수동개입여부에 O 표시 되어있는 column들은 제외하였습니다.**

	1) 이 코드에서는 원본 데이터를 10 % 의 Test txt 파일과 90 % 의 Train 파일로 나누어 줍니다.
	2) test와 train data는 Train의 평균과 분산을 따라서 표준정규분포에 의해 정규화됩니다. 
	3) 원본 데이터에서 문자열(character)과 카테고리(category)는 벡터화됩니다.
	4) 원본 데이터에서 F1~F7+수동개입여부에 해당하는 column은 모델을 통해 얻게 될 결과값들과 비교하기 위해 _validation.txt에 가공되지 않고 기록되어집니다.
	5) 마지막으로 meta.txt 파일에 문자열(character) 과 카테고리(category) column들을 벡터화 할 때 
	   각각 원본 데이터에서 몇 번째 열의 데이터인지(index)를 포함하도록 해 놓았습니다.
	  ex) 0,273 <-- 0번 째 칼럼의 열은 273dim의 vector라는 의미입니다.

* 실행방법 *

execute.py를 실행하면 after_processing 폴더에 5개의 ouput file이 생성됩니다.