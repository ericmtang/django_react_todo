import { cleanup, render, screen } from '@testing-library/react';
import App from './App';

test('renders ToDo App screen', () => {
  render(<App />);
  const linkElement = screen.getByText(/ToDo App/i);
  expect(linkElement).toBeInTheDocument();
});


