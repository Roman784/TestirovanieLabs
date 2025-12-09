// Простой пример
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const message: string = greet("TypeScript");
console.log(message);

// Пример с интерфейсом
interface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "John Doe",
  email: "john@example.com"
};

console.log(`User: ${user.name}, Email: ${user.email}`);