import { cleanup, render, screen } from '@testing-library/react';
import App from './App';

test('renders ToDo App screen', () => {
  render(<App />);
  const title = screen.getByText(/ToDo App/i);
  expect(title).toBeInTheDocument();
});

test('renders Add Task button', () => {
  render(<App />);
  const addButton = screen.getByRole('button', {name: /Add Task/i});
  expect(addButton).toBeInTheDocument();
});

// test('renders Milk todo item', () => {
//   render(<App />);
//   const linkElement = screen.getByText(/Get Some Milk/i);
//   expect(linkElement).toBeInTheDocument();
// });

afterAll(() => cleanup());