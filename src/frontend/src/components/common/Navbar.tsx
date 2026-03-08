'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';

export default function Navbar() {
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    setIsLoggedIn(!!localStorage.getItem('token'));
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user_id');
    setIsLoggedIn(false);
    router.push('/login');
  };

  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Link href="/" className="text-xl font-bold text-blue-600">
                TodoApp
              </Link>
            </div>
            {isLoggedIn && (
              <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                <Link
                  href="/tasks"
                  className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                >
                  任务列表
                </Link>
                <Link
                  href="/dashboard"
                  className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                >
                  仪表盘
                </Link>
              </div>
            )}
          </div>
          <div className="flex items-center">
            {isLoggedIn ? (
              <button
                onClick={handleLogout}
                className="ml-8 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                退出登录
              </button>
            ) : (
              <div className="flex space-x-4">
                <Link
                  href="/login"
                  className="text-gray-500 hover:text-gray-700 px-3 py-2 rounded-md text-sm font-medium"
                >
                  登录
                </Link>
                <Link
                  href="/register"
                  className="bg-blue-600 text-white hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium"
                >
                  注册
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}
