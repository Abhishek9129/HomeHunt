import React,{useState} from "react";
import axios from "axios";

const Login=()=>{
    const [email,setEmail]=useState("");
    const [password,setPassword]=useState("");

    const handleSubmit=async(e)=>{
        try{
        const response=await axios.post("http://localhost:8000/auth/login",{email,password});
        alert(response.data.message);
        }
        catch(error)
        {
        alert(error.response.data.detail);
        }
    }
    return (
      <div>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="email"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        ></input>
        <input
          type="text"
          placeholder="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        ></input>
        <button type="submit">Login</button>
        </form>
              </div>
    );
}
export default Login;