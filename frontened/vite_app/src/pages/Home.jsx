import React from "react";
import { LogIn, UserPlus } from "lucide-react";
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 to-blue-300">
      <h1 className="text-4xl font-bold mb-8 text-gray-800">
        Welcome to My App
      </h1>

      <div className="flex space-x-10">
        {/* Login */}
        <button
          onClick={() => navigate("/login")}
          className="flex flex-col items-center p-6 bg-white rounded-2xl shadow-lg hover:bg-blue-50 transition"
        >
          <LogIn className="w-12 h-12 text-blue-600 mb-2" />
          <span className="text-lg font-medium text-blue-700">Login</span>
        </button>

        {/* Register */}
        <button
          onClick={() => navigate("/register")}
          className="flex flex-col items-center p-6 bg-white rounded-2xl shadow-lg hover:bg-green-50 transition"
        >
          <UserPlus className="w-12 h-12 text-green-600 mb-2" />
          <span className="text-lg font-medium text-green-700">Register</span>
        </button>
      </div>
    </div>
  );
}

export default Home;
