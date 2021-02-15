#### 실시간 검색어 확인하기

>  * requests           
>    import requests       
> 
>    response = requests.get(url)
>    ``` 
>       해당 url서버에 get요청          
>       요청값으로 "응답"을 받음    
>    ```

- 응답값을 예쁘게 출력 - 
>   * beautifulSoup [bs4 모듈의 '기능']         
>       from bs4 import BeautifulSoup       
>       
>       **bs4와 같은 외부모듈을 사용하기위해서는 내 컴퓨터에 설치!**    
>
>       soup = BeautifulSoup(response.text, 'html.paser')       
>       ```
>           BeautifulSoup(데이터, 파싱방법)             
>           데이터 : (html, xml)이 올 수 있음       
>           parshing : 데이터를 의미있게 변경       
>           pasher : 파싱을 도와주는 애들       
>               (html.paser -> 파이썬에 내장되어있는 파서)      
>       ```
>
>       results = soup.findAll('a','link_favorsch')         
>       ```
>           a태그안에 link_favorsch를 가진 애들을 찾아라    
>       ```

- 우리는 로봇이 아니에요 -
> 네이버 처럼 로봇같은 애들을 막아두는 사이트들이 있음      
> 이때 사용하는 것      
>
> ````
>   headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/  
>   537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
> ````
>
>   * response = requests.get(url,headers=headers)        
>   ```
>       requests.get으로 요청을 보낼때 우리의 정보(headers)도 같이 보내줌
>   ```


`
`
### requeste 모듈 import 하기 (with Anaconda)
1. cmd 창에서 파이썬이 설치된 파일로 이동    
2. 'pip install requests' 로 requests모듈 import하기    

**아나콘다의 파이썬을 이용하는 경우**         
```
'conda install -c anaconda requests'      
```



 _!환경변수에 파이썬이 등록되어있는지도 꼭 확인하기!_



