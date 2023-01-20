import logo from './logo.svg';
import './App.css';
function Header(props){
  return <header>
    <h1>{props.title}</h1>
  </header>
}
function Nav(props){
  const lis=[]
  for(let i=0; i<props.explain.length; i++){
    let app=props.explain[i];
    lis.push(<li key={app.id}>
      <a id={app.id}>{app.title}</a>
    </li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(){
  return <article>
    <h2>How is it?</h2>
  </article>
}
function App(props) {
  const explain=[
    {id:1, title:"Routin App", body:"It's ..."},
    {id:2, title:"Plan App", body:"It's ..."}
  ]
  return (
    <div className="App">
      <Header title="Hello"></Header>
      <Nav explain={explain}></Nav>
      <Article></Article>
    </div>
  );
}

export default App;
