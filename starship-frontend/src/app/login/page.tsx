"use client";
import { useState, FormEvent } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useRouter } from 'next/navigation';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    await login(username, password);
    // redirect to /starships when we login
    router.push('/starships');
  };

  return (
    <div className='w-full max-w-xs'>
      <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
    
      <div className="mb-4">
      <label className="block text-gray-700 text-sm font-bold mb-2"  htmlFor="username">
        Username
      </label>
      <input id="username" type="text" value={username} onChange={(e) => setUsername(e.target.value)} className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"  placeholder="Username" />
    </div>

     
      <div className="mb-4">
        <label>Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <button className='btn' type="submit">Login</button>
    </form>
    </div>
  );
};

export default Login;
