import {useState} from "react";

import "./App.css";

import Sidebar from "./components/Sidebar";

import ChatWindow from "./components/ChatWindow";

function App(){

const [reset,setReset]=useState(0);
const [theme,setTheme]=useState("dark");

function newChat(){

setReset(prev=>prev+1);

}

return(

<div className={`app ${theme}`}>

<Sidebar

newChat={newChat}

theme={theme}

setTheme={setTheme}

/>

<ChatWindow reset={reset}/>

</div>

);

}

export default App;