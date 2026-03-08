'use client';

import Link from 'next/link';
import { useEffect, useState } from 'react';

export default function HomePage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    setIsLoggedIn(!!localStorage.getItem('token'));
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] text-center px-4">
      <h1 className="text-5xl font-extrabold text-gray-900 mb-6">
        轻松管理您的 <span className="text-blue-600">每一天</span>
      </h1>
      <p className="text-xl text-gray-600 mb-10 max-w-2xl">
        一款简单、高效的 Todo 应用，助您有条不紊地完成各项任务，提升工作效率。
      </p>
      
      <div className="flex space-x-4">
        {isLoggedIn ? (
          <Link
            href="/tasks"
            className="px-8 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition duration-300 shadow-lg"
          >
            开始管理任务
          </Link>
        ) : (
          <>
            <Link
              href="/register"
              className="px-8 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition duration-300 shadow-lg"
            >
              立即注册
            </Link>
            <Link
              href="/login"
              className="px-8 py-3 bg-white text-blue-600 border border-blue-600 rounded-lg font-semibold hover:bg-blue-50 transition duration-300"
            >
              登录
            </Link>
          </>
        )}
      </div>

      <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-5xl">
        <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 bg-blue-100 text-blue-600 rounded-lg flex items-center justify-center mb-4 mx-auto">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
            </svg>
          </div>
          <h3 className="text-lg font-bold mb-2 text-gray-900">任务管理</h3>
          <p className="text-gray-500">快速创建、更新和删除您的日常任务。</p>
        </div>
        
        <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 bg-green-100 text-green-600 rounded-lg flex items-center justify-center mb-4 mx-auto">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h3 className="text-lg font-bold mb-2 text-gray-900">数据统计</h3>
          <p className="text-gray-500">清晰的仪表盘展示您的完成情况。</p>
        </div>
        
        <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 bg-purple-100 text-purple-600 rounded-lg flex items-center justify-center mb-4 mx-auto">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
          <h3 className="text-lg font-bold mb-2 text-gray-900">安全可靠</h3>
          <p className="text-gray-500">基于 JWT 的认证，保护您的私有数据。</p>
        </div>
      </div>
    </div>
  );
}
