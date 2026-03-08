'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { apiRequest } from '@/lib/api';
import { Task } from '@/types';

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [newTitle, setNewTitle] = useState('');
  const [newDesc, setNewDesc] = useState('');
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
      return;
    }
    fetchTasks();
  }, [router]);

  const fetchTasks = async () => {
    try {
      const data = await apiRequest<Task[]>('/api/tasks/');
      setTasks(data);
    } catch (err: any) {
      setError(err.message || '获取任务失败');
    } finally {
      setLoading(false);
    }
  };

  const addTask = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;

    try {
      const task = await apiRequest<Task>('/api/tasks/', {
        method: 'POST',
        body: JSON.stringify({
          title: newTitle,
          description: newDesc,
        }),
      });
      setTasks([task, ...tasks]);
      setNewTitle('');
      setNewDesc('');
    } catch (err: any) {
      alert(err.message || '添加任务失败');
    }
  };

  const toggleTaskStatus = async (task: Task) => {
    const newStatus = task.status === 'pending' ? 'completed' : 'pending';
    try {
      const updatedTask = await apiRequest<Task>(`/api/tasks/${task.id}`, {
        method: 'PUT',
        body: JSON.stringify({
          ...task,
          status: newStatus,
        }),
      });
      setTasks(tasks.map((t) => (t.id === task.id ? updatedTask : t)));
    } catch (err: any) {
      alert(err.message || '更新状态失败');
    }
  };

  const deleteTask = async (id: number) => {
    if (!confirm('确定要删除这个任务吗？')) return;
    try {
      await apiRequest(`/api/tasks/${id}`, { method: 'DELETE' });
      setTasks(tasks.filter((t) => t.id !== id));
    } catch (err: any) {
      alert(err.message || '删除任务失败');
    }
  };

  if (loading) return <div className="text-center py-10 text-black">加载中...</div>;

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-8 text-gray-900">我的任务清单</h1>

      {/* 添加任务表单 */}
      <form onSubmit={addTask} className="bg-white p-6 rounded-lg shadow-sm mb-8 border border-gray-200">
        <div className="space-y-4">
          <div>
            <input
              type="text"
              placeholder="任务标题..."
              value={newTitle}
              onChange={(e) => setNewTitle(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 text-black"
              required
            />
          </div>
          <div>
            <textarea
              placeholder="任务描述 (可选)..."
              value={newDesc}
              onChange={(e) => setNewDesc(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 text-black"
              rows={2}
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition duration-200"
          >
            添加新任务
          </button>
        </div>
      </form>

      {error && <div className="bg-red-50 text-red-600 p-4 rounded-md mb-6">{error}</div>}

      {/* 任务列表 */}
      <div className="space-y-4">
        {tasks.length === 0 ? (
          <p className="text-center text-gray-500 py-10">暂无任务，快去添加一个吧！</p>
        ) : (
          tasks.map((task) => (
            <div
              key={task.id}
              className={`flex items-center justify-between p-4 bg-white rounded-lg shadow-sm border ${
                task.status === 'completed' ? 'border-green-100 bg-green-50' : 'border-gray-200'
              }`}
            >
              <div className="flex items-center space-x-4 flex-1">
                <input
                  type="checkbox"
                  checked={task.status === 'completed'}
                  onChange={() => toggleTaskStatus(task)}
                  className="h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500 cursor-pointer"
                />
                <div className="flex-1">
                  <h3
                    className={`font-medium ${
                      task.status === 'completed' ? 'line-through text-gray-400' : 'text-gray-900'
                    }`}
                  >
                    {task.title}
                  </h3>
                  {task.description && (
                    <p className={`text-sm ${task.status === 'completed' ? 'text-gray-300' : 'text-gray-500'}`}>
                      {task.description}
                    </p>
                  )}
                </div>
              </div>
              <button
                onClick={() => deleteTask(task.id)}
                className="ml-4 text-red-500 hover:text-red-700 p-2"
                title="删除任务"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                  />
                </svg>
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
