## 1.게임의 소개
         - 게임 이름 : Hell taker  
         - 게임 소개 : 소코반과 비슷한 퍼즐 플레이 게임 , ![hell](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRl_QFWlCf6pnCqtF83fhbUBLVG9aZpmQMOwg&usqp=CAU)  
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
         
