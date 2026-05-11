const API_BASE = '/api';

function getToken() {
    return localStorage.getItem('access_token');
}

function getUser() {
    const u = localStorage.getItem('current_user');
    return u ? JSON.parse(u) : null;
}

function setAuth(data) {
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
    localStorage.setItem('current_user', JSON.stringify(data.user));
}

function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('current_user');
    window.location.href = '/login/';
}

async function apiFetch(path, options = {}) {
    const token = getToken();
    const headers = { 'Content-Type': 'application/json', ...options.headers };
    if (token) headers['Authorization'] = 'Bearer ' + token;

    const res = await fetch(API_BASE + path, { ...options, headers });

    if (res.status === 401) {
        // Try refresh
        const refresh = localStorage.getItem('refresh_token');
        if (refresh) {
            const r2 = await fetch(API_BASE + '/auth/token/refresh/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ refresh }),
            });
            if (r2.ok) {
                const d = await r2.json();
                localStorage.setItem('access_token', d.access);
                headers['Authorization'] = 'Bearer ' + d.access;
                return fetch(API_BASE + path, { ...options, headers });
            }
        }
        logout();
        return;
    }
    return res;
}

function requireAuth() {
    if (!getToken()) {
        window.location.href = '/login/';
    }
}

function requireAdmin() {
    const user = getUser();
    if (!getToken() || !user || user.role !== 'admin') {
        window.location.href = '/login/';
    }
}
