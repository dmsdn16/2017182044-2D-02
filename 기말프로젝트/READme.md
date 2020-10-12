## 1.게임의 소개
         - 게임 이름 : Hell taker  
         - 게임 소개 : 소코반과 비슷한 퍼즐 플레이 게임 
   ![hell](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRl_QFWlCf6pnCqtF83fhbUBLVG9aZpmQMOwg&usqp=CAU)  
         - 게임의 목적은 미로를 탈출하는 것이며, 게임 방법은 키보드를 이용하여 방해물들을 제거하며 정해진 이동횟수안에 정해진 위치에 도달하는 것이다.  
  ## 2.GAME STATE
         - 로고 화면, 메인 화면, 옵션,메뉴얼,게임 맵, 클리어축하  
         - 총 스테이트 수 : 6개
  ## 3.STATE 평
  
         - 로고 : 로고를 표시한다
  
         - 메인 화면 : new game, load game, option, manuel 선택창을 표시
  
         - 옵션 : 사운드를 관리하는 scene
         
         - 메뉴얼 : 게임 플레이방법을 설명하는 scene
         
         - 게임 맵 : 플레이어가 게임을 플레이하는 scene으로 클리어하면 다음 맵으로 넘어가며
           보스 맵을 클리어하면 클리어화면으로 넘어간다
           
         - 클리어축하 : 클리어를 축하해주는 이미지를 나타내는 scene
         
  #### state
         - 필요객체 : 파괴 불가 오브젝트, 파괴 가능오브젝트, 플레이어, 엔드 지점
![파이썬 다이그램](https://user-images.githubusercontent.com/32299218/94264634-fa109700-ff71-11ea-925a-e262598dae53.png)


 ## 게임흐름
         - 카운트 다운이 0읻되기 전까지 도착지점에 도달해야 한다
![map](https://user-images.githubusercontent.com/32299218/95701110-aac1aa80-0c83-11eb-9024-965ae724b114.png)

          - 다음은 각각 장애물을 격파하는 장면, 이동시키는 장면, 실패하는 장면입니다
 ![장애물 격파](https://user-images.githubusercontent.com/32299218/95701164-cd53c380-0c83-11eb-9bbd-6721fe02e7ea.jpg)
 ![장애물 이동](https://user-images.githubusercontent.com/32299218/95701186-d80e5880-0c83-11eb-9d78-10ac4a7b6c17.jpg)
 ![실패](https://user-images.githubusercontent.com/32299218/95701207-e492b100-0c83-11eb-9437-7e9338e4e7e8.jpg)
## 필요한 기술
       - 다른 과목에서 배운 기술 : 사운드 관리 , 객체지향
       - 현 과목에서 배운 기술 ; 프레임 관리, 이미지 관리 , 키보드 입력 관리
       마우스 관리
## 개발범위
     
![스크린샷(264)](https://user-images.githubusercontent.com/32299218/95700875-0a6b8600-0c83-11eb-89cb-0d7397b85bcd.png)

## 개발일정
![스크린샷(265)](https://user-images.githubusercontent.com/32299218/95700954-3dae1500-0c83-11eb-98f4-51fa1e667971.png)



         
