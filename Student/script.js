document.addEventListener('DOMContentLoaded', function() {
    const studentForm = document.getElementById('studentForm');
    const messageDiv = document.getElementById('message');
    const studentTable = document.getElementById('studentTable').getElementsByTagName('tbody')[0];
    const downloadBtn = document.getElementById('downloadBtn');
    
    // Load existing data from localStorage
    let students = JSON.parse(localStorage.getItem('students')) || [];
    displayStudents();

    studentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const student = {
            name: document.getElementById('name').value,
            rollNo: document.getElementById('rollNo').value,
            age: document.getElementById('age').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            grade: document.getElementById('grade').value,
            address: document.getElementById('address').value
        };

        // Add student to array
        students.push(student);
        
        // Save to localStorage
        localStorage.setItem('students', JSON.stringify(students));
        
        // Display success message
        showMessage('Student information saved successfully!', 'success');
        
        // Update table
        displayStudents();
        
        // Reset form
        studentForm.reset();
    });

    downloadBtn.addEventListener('click', function() {
        downloadExcel();
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = type;
        setTimeout(() => {
            messageDiv.textContent = '';
            messageDiv.className = '';
        }, 3000);
    }

    function displayStudents() {
        studentTable.innerHTML = '';
        students.forEach(student => {
            const row = studentTable.insertRow();
            Object.values(student).forEach(text => {
                const cell = row.insertCell();
                cell.textContent = text;
            });
        });
    }

    function downloadExcel() {
        // Create CSV content
        const headers = ['Name', 'Roll No', 'Age', 'Email', 'Phone', 'Grade', 'Address'];
        let csvContent = headers.join(',') + '\n';
        
        students.forEach(student => {
            const row = [
                `"${student.name}"`,
                `"${student.rollNo}"`,
                `"${student.age}"`,
                `"${student.email}"`,
                `"${student.phone}"`,
                `"${student.grade}"`,
                `"${student.address}"`
            ];
            csvContent += row.join(',') + '\n';
        });

        // Create and download the file
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', 'student_records.csv');
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
});