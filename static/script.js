const API_URL = 'http://localhost:5000/api/students';

document.getElementById('studentForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const course = document.getElementById('course').value;

  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, course })
  });

  document.getElementById('studentForm').reset();
  loadStudents();
});

async function loadStudents() {
  const res = await fetch(API_URL);
  const students = await res.json();
  const list = document.getElementById('studentList');

  list.innerHTML = '';
  students.forEach(s => {
    const li = document.createElement('li');
    li.innerHTML = `${s.name} (${s.course}) <button onclick="deleteStudent(${s.id})">❌</button>`;
    list.appendChild(li);
  });
}

async function deleteStudent(id) {
  await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
  loadStudents();
}

window.onload = loadStudents;
