import logo from './logo.svg';
import './App.css';
// UI를 편집하는 곳 

// header를 불러오는 함수, 컴포넌트
function Header(props){  
  console.log('props', props, props.title) // console을 보면 props에 title: 'REACT'가 있는 것을 볼 수 있다.
  // { }를 이용하여 문자열을 가져오는 것이 아니라 props.title값을 가져온다.
  return <header>
    <h1><a href="/">{props.title}</a></h1> 
  </header>
}

function Nav(props){
  const lis=[]
  for(let i=0; i<props.topics.length; i++){
    let t=props.topics[i];
    lis.push(<li key={t.id}><a href={'/read/'+t.id}>{t.title}</a></li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(props){
  return <article>
  <h2>{props.title}</h2>
  {props.body}
</article>
}
function App() {
  const topics = [ // const로 값이 변하지 않는 변수 topics 생성
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'js is ...'}
  ]
  return (
    <div>
      <Header title="REACT"></Header>
      <Nav topics={topics}></Nav>
      <Article title="Welcome" body="Hello, WEB"></Article>
      <Article title="Hi" body="Hello, REACT"></Article>
    </div>
  );
}

export default App;
