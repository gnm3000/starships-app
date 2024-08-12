import { ReactNode } from 'react';
import { AuthProvider } from '../context/AuthContext';
import '../globals.css';

export const metadata = {
  title: 'Starships App',
  description: 'A Starships listing app with authentication',
};
// we wrap the table starship with our AuthProvider
export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
