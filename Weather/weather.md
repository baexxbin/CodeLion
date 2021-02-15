#### 날씨 정보 받아오기

- API -    
> API(Application Programming Interface): 프로그램과 프로그램을 이어주는 인터페이스      
> * 클라이언트와 서버가 데이터를 원활히 주고받기 위해 API 존재    
> " 사용자가 만드는 프로그램과 기존의 프로그램을 연결하는 역할 "    
> API를 만든다: 사용자가 필요로하는 기능 만들고, 서버에 올린후, 특정 규약에 따라 사용할 수 있도록 함.       
> API를 사용한다: 누군가가 만들어놓은 기능을 특정 규약에 맞춰 사용 함.    
 
> apikey = "################################"
> ``` 
>    API요청을 보낼 "서버주소"    
>      (공통url)?(파라미터)     
>       (공통url) 이러한 주소로 요청을 보내되, (파라미터) 로 보낸 정보를 가져가서 응답을 해줘!      
>       + 파라미터는 (&)기호로 연결
> ``` 


- json -    
json: javascript object notation [자바스크립트 객체의 문법을 따르는 문자기반의 데이터 포맷]    
==> 데이터를 주고받을 때 사용하는 포맷     

* 일반문자열을 json타입으로 변환하기     
    : json.loads(str)     
    