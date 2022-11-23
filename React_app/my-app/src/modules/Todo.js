import React from 'react';
import axios from "axios";
import { useState} from 'react';
import { useEffect } from 'react';
const Todo = () => {
   const [TaskObj, setTaskObj] = React.useState([]);
   const [Body, setBody] = React.useState("");
   
    const onClickShowAll=() => {
      axios.get("/todo").then((res) => {
        setTaskObj(res.data);
      });
    };

    function deleteTask(id)
    {
      fetch(`/todo/${id}`,{
        method:'DELETE'
      }).then((res)=>{
        res.json().then((data)=>{
          console.warn(data)
          
        })
      })
    }

  
    function saveTask(){
      console.warn({Body});
      let data = {Body}
      axios.post("/todo",{
        body:data.Body
        
      }).then((result)=>{
        //console.warn("result",result);
        result.json().then((resp)=>{
          console.warn("resp",resp)
        })
      })
     
    }

    console.log(TaskObj)
    return (
        <div className="App">
          <h2>TODO APP 📫</h2>
          <table class="center" border={2}><tr>
            <th>TODO ID</th>
            <th>TASK</th>
            <th>DELETE OPERATION</th></tr>
          {TaskObj.map((post) => {
             return (
                <tr>
                   <td className="post-title">{post.id}</td>
                   <td className="post-body">{post.body}</td>
                   <td><button onClick={()=>deleteTask(post.id)}>Delete</button></td>
                   
                </tr>
                
             );
          })}
          </table>
          <button onClick={onClickShowAll}>show all todo</button><br />
          <h4>Enter new task</h4><input type="json" value={Body} onChange={(e)=>{setBody(e.target.value)}} name="Body"/>
          <button type="button" onClick={saveTask}>save task</button>
        </div>
        
        );

        



      };

      
 export default Todo;

 