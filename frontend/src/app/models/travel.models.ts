export interface Trip {
  id?: number;
  title: string;
  destination: string;
  description: string;
  start_date: string;
  end_date: string;
  budget: number;
  status: 'planned' | 'active' | 'completed' | 'cancelled';
  cover_image: string;
  total_expenses?: number;
  remaining_budget?: number;
  booking_count?: number;
  bookings?: Booking[];
  expenses?: Expense[];
  itinerary?: ItineraryItem[];
  created_at?: string;
  updated_at?: string;
}

export interface Booking {
  id?: number;
  trip: number;
  title: string;
  booking_type: 'flight' | 'hotel' | 'car' | 'activity' | 'other';
  provider: string;
  confirmation_number: string;
  amount: number;
  booking_date: string;
  status: 'pending' | 'confirmed' | 'cancelled';
  notes: string;
}

export interface Expense {
  id?: number;
  trip: number;
  title: string;
  category: 'transport' | 'accommodation' | 'food' | 'entertainment' | 'shopping' | 'other';
  amount: number;
  date: string;
  notes: string;
}

export interface ItineraryItem {
  id?: number;
  trip: number;
  day: number;
  title: string;
  time: string | null;
  location: string;
  description: string;
}

export interface DashboardStats {
  total_trips: number;
  active_trips: number;
  planned_trips: number;
  completed_trips: number;
  total_budget: number;
  total_expenses: number;
  total_bookings: number;
  destinations: { destination: string; count: number }[];
}
