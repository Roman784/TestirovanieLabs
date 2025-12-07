interface Task {
    id: number;
    text: string;
    urgent: boolean;
    completed: boolean;
}

class Todo {
    private tasks: Task[] = [];
    private nextId: number = 1;

    private taskInput!: HTMLInputElement;
    private urgentCheckbox!: HTMLInputElement;
    private addButton!: HTMLButtonElement;
    private tasksList!: HTMLUListElement;

    constructor() {
        this.initializeElements();
        this.setupEventListeners();
        this.loadFromStorage();
        this.renderTasks();
    }

    private initializeElements(): void {
        this.taskInput = document.getElementById('taskInput') as HTMLInputElement;
        this.urgentCheckbox = document.getElementById('urgentCheckbox') as HTMLInputElement;
        this.addButton = document.getElementById('addTaskBtn') as HTMLButtonElement;
        this.tasksList = document.getElementById('tasksList') as HTMLUListElement;
    }

    private setupEventListeners(): void {
        this.addButton.addEventListener('click', () => this.addTask());
        
        this.taskInput.addEventListener('keypress', (e: KeyboardEvent) => {
            if (e.key === 'Enter') this.addTask();
        });
    }

    private addTask(): void {
        const text = this.taskInput.value.trim();

        // Нет проверки, заполнено ли поле.

        const newTask: Task = {
            id: this.nextId++,
            text: text,
            urgent: this.urgentCheckbox.checked,
            completed: false
        };

        this.tasks.push(newTask);
        
        // Не очищается поле задачи.
        // Тогл срочности не выключается.
        
        this.saveToStorage();
        this.renderTasks();
    }

    private deleteTask(id: number): void {
        this.tasks = this.tasks.filter(task => task.id !== id);
        this.saveToStorage();
        this.renderTasks();
    }

    private toggleTask(id: number): void {
        const task = this.tasks.find(task => task.id === id);
        if (task) {
            // Можно переключить только в одну сторону. 
            if (!task.completed)
                task.completed = true;
            this.saveToStorage();
            this.renderTasks();
        }
    }

    private renderTasks(): void {
        this.tasksList.innerHTML = '';
        
        if (this.tasks.length === 0) {
            const emptyMessage = document.createElement('li');
            emptyMessage.textContent = 'Нет задач. Добавьте первую!';
            emptyMessage.style.textAlign = 'center';
            emptyMessage.style.color = '#999';
            emptyMessage.style.padding = '20px';
            this.tasksList.appendChild(emptyMessage);
            return;
        }

        this.tasks.forEach(task => {
            const li = document.createElement('li');
            li.className = `task-item ${task.urgent ? 'urgent' : ''} ${task.completed ? 'completed' : ''}`;
            li.dataset.id = task.id.toString();

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'task-checkbox';
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', () => this.toggleTask(task.id));

            const text = document.createElement('span');
            text.className = 'task-text';
            text.textContent = task.text;

            if (task.urgent) {
                const urgentLabel = document.createElement('span');
                urgentLabel.className = 'urgent-label';
                urgentLabel.textContent = 'Срочно';
                li.appendChild(urgentLabel);
            }

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = '×';
            deleteBtn.addEventListener('click', () => this.deleteTask(task.id));

            li.appendChild(checkbox);
            li.appendChild(text);
            li.appendChild(deleteBtn);
            this.tasksList.appendChild(li);
        });
    }

    private saveToStorage(): void {
        localStorage.setItem('tasks', JSON.stringify(this.tasks));
        localStorage.setItem('nextId', this.nextId.toString());
    }

    private loadFromStorage(): void {
        const savedTasks = localStorage.getItem('tasks');
        const savedNextId = localStorage.getItem('nextId');

        if (savedTasks) {
            this.tasks = JSON.parse(savedTasks);
        }

        // Не загружается id следующей таски.
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Todo();
});