'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { apiRequest } from '@/lib/api';
import { DashboardStats } from '@/types';

export default function DashboardPage() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
      return;
    }
    fetchStats();
  }, [router]);

  const fetchStats = async () => {
    try {
      const data = await apiRequest<DashboardStats>('/api/dashboard/stats');
      setStats(data);
    } catch (err) {
      console.error('获取统计失败', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center py-10 text-black">加载中...</div>;

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-8 text-gray-900">数据概览</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p className="text-sm font-medium text-gray-500 uppercase">总任务数</p>
          <p className="mt-2 text-3xl font-bold text-gray-900">{stats?.total_tasks || 0}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-sm border border-green-200 bg-green-50">
          <p className="text-sm font-medium text-green-600 uppercase">已完成</p>
          <p className="mt-2 text-3xl font-bold text-green-700">{stats?.completed_tasks || 0}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-sm border border-blue-200 bg-blue-50">
          <p className="text-sm font-medium text-blue-600 uppercase">进行中</p>
          <p className="mt-2 text-3xl font-bold text-blue-700">{stats?.pending_tasks || 0}</p>
        </div>
      </div>

      <div className="mt-12 bg-white p-8 rounded-lg shadow-sm border border-gray-200 text-center">
        <h2 className="text-xl font-semibold mb-4 text-gray-900">继续努力！</h2>
        <p className="text-gray-600 mb-6">
          您当前有 {stats?.pending_tasks || 0} 个任务待处理。
        </p>
        <button
          onClick={() => router.push('/tasks')}
          className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700"
        >
          前往任务列表
        </button>
      </div>
    </div>
  );
}
