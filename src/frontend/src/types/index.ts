export interface User {
  id: number;
  username: string;
  email: string;
}

export interface Task {
  id: number;
  title: string;
  description: string | null;
  status: 'pending' | 'completed';
  created_at: string;
  updated_at: string;
}

export interface DashboardStats {
  total_tasks: number;
  completed_tasks: number;
  pending_tasks: number;
}

export interface ApiResponse<T> {
  code: number;
  message: string;
  data: T;
}
