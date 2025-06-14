document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const filter = tab.getAttribute('data-filter');

    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    document.querySelectorAll('.kanban-column').forEach(column => {
      if (filter === 'all' || column.dataset.status === filter) {
        column.style.display = 'block';
      } else {
        column.style.display = 'none';
      }
    });
  });
});

// Dropdown toggle logic
document.querySelectorAll('.menu-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const dropdown = btn.nextElementSibling;
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
  });
});

// Close dropdown if clicking outside
window.addEventListener('click', e => {
  if (!e.target.matches('.menu-btn')) {
    document.querySelectorAll('.dropdown').forEach(d => d.style.display = 'none');
  }
});
document.getElementById('openTaskModal').addEventListener('click', () => {
  document.getElementById('taskModal').style.display = 'flex';
});

document.getElementById('closeModal').addEventListener('click', () => {
  document.getElementById('taskModal').style.display = 'none';
});

document.getElementById('closeModalBtn').addEventListener('click', () => {
  document.getElementById('taskModal').style.display = 'none';
});
