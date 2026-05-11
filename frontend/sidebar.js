(function () {
    var token   = localStorage.getItem('access_token');
    var userStr = localStorage.getItem('current_user');
    var path    = window.location.pathname;

    // Guest (no login) — asosiy linklar
    var role     = null;
    var fullname = '';

    if (token && userStr) {
        try {
            var user = JSON.parse(userStr);
            role     = user ? user.role : null;
            fullname = user ? (user.fullname || '') : '';
        } catch (e) {}
    }

    // Asosiy linklar — hammaga
    var links = [
        { href: '/',            icon: 'fa-home',         label: 'Bosh sahifa'        },
        { href: '/pasport/',    icon: 'fa-id-card',      label: "Mahalla mas'ullari"  },
        { href: '/xizmatlar/',  icon: 'fa-briefcase',    label: 'Xizmatlar'           },
        { href: '/murojaat/',   icon: 'fa-paper-plane',  label: 'Murojaat yuborish'   },
    ];

    // Mas'ul xodim uchun qo'shimcha
    if (role === 'responsible') {
        links.push({ href: '/kabinet/', icon: 'fa-inbox', label: 'Murojatlarim' });
    }

    // Admin uchun qo'shimcha
    if (role === 'admin') {
        links.push({ href: '/admin-panel/', icon: 'fa-shield-halved', label: 'Admin panel' });
        links.push({ href: '/admin-panel/xabarlar/', icon: 'fa-list-check', label: 'Barcha murojatlar' });
    }

    var navItems = links.map(function (l) {
        var active = (l.href === '/' ? path === '/' : path.indexOf(l.href) === 0) ? 'msb-active' : '';
        return '<a href="' + l.href + '" class="msb-link ' + active + '">' +
            '<i class="fas ' + l.icon + '"></i><span>' + l.label + '</span></a>';
    }).join('');

    // Bottom user section
    var bottomHtml;
    if (role && fullname) {
        var initials = fullname.trim().split(' ').slice(0, 2).map(function (w) { return w[0]; }).join('').toUpperCase();
        var roleLabel = role === 'admin' ? 'Administrator' : role === 'responsible' ? "Mas'ul xodim" : 'Foydalanuvchi';
        bottomHtml =
            '<div class="msb-bottom">' +
            '<div class="msb-avatar">' + initials + '</div>' +
            '<div class="msb-info"><div class="msb-name">' + fullname.split(' ').slice(0, 2).join(' ') + '</div>' +
            '<div class="msb-role">' + roleLabel + '</div></div>' +
            '<button class="msb-logout" onclick="msbLogout()" title="Chiqish"><i class="fas fa-sign-out-alt"></i></button>' +
            '</div>';
    } else {
        bottomHtml =
            '<div class="msb-bottom">' +
            '<a href="/kabinet/" class="msb-login-btn"><i class="fas fa-sign-in-alt"></i><span>Kirish</span></a>' +
            '</div>';
    }

    var html =
        '<div id="masul-sidebar">' +
        '<div class="msb-logo"><i class="fas fa-building-shield"></i>' +
        '<div><div style="font-size:14px;font-weight:800;line-height:1.2">OLTOG\'IL</div>' +
        '<div style="font-size:10px;opacity:.7;letter-spacing:1px">MAHALLASI</div></div></div>' +
        '<nav class="msb-nav">' + navItems + '</nav>' +
        bottomHtml +
        '</div>';

    var css =
        '#masul-sidebar{position:fixed;top:0;left:0;width:220px;height:100vh;background:#1e3c72;' +
        'display:flex;flex-direction:column;z-index:9999;box-shadow:3px 0 16px rgba(0,0,0,.25);}' +

        '.msb-logo{display:flex;align-items:center;gap:11px;padding:20px 18px 16px;color:#fff;' +
        'border-bottom:1px solid rgba(255,255,255,.1);}' +
        '.msb-logo i{font-size:26px;color:#7eb8ff;}' +

        '.msb-nav{flex:1;padding:12px 0;overflow-y:auto;}' +
        '.msb-link{display:flex;align-items:center;gap:12px;padding:13px 20px;color:rgba(255,255,255,.75);' +
        'text-decoration:none;font-size:14px;font-weight:500;border-left:3px solid transparent;transition:all .15s;}' +
        '.msb-link i{width:18px;text-align:center;font-size:15px;flex-shrink:0;}' +
        '.msb-link:hover{background:rgba(255,255,255,.09);color:#fff;border-left-color:rgba(255,255,255,.4);}' +
        '.msb-active{background:rgba(255,255,255,.15)!important;color:#fff!important;border-left-color:#7eb8ff!important;}' +

        '.msb-bottom{display:flex;align-items:center;gap:9px;padding:14px;border-top:1px solid rgba(255,255,255,.1);}' +
        '.msb-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#4a90d9,#7eb8ff);' +
        'display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:700;flex-shrink:0;}' +
        '.msb-info{flex:1;min-width:0;}' +
        '.msb-name{color:#fff;font-size:13px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}' +
        '.msb-role{color:rgba(255,255,255,.5);font-size:11px;}' +
        '.msb-logout{background:rgba(255,255,255,.1);border:none;color:rgba(255,255,255,.65);' +
        'width:30px;height:30px;border-radius:8px;cursor:pointer;font-size:13px;flex-shrink:0;}' +
        '.msb-logout:hover{background:rgba(231,76,60,.5);color:#fff;}' +
        '.msb-login-btn{display:flex;align-items:center;gap:10px;color:rgba(255,255,255,.75);text-decoration:none;' +
        'font-size:14px;font-weight:600;padding:8px 12px;border-radius:8px;background:rgba(255,255,255,.1);' +
        'width:100%;transition:background .15s;}' +
        '.msb-login-btn:hover{background:rgba(255,255,255,.2);color:#fff;}' +

        'body{margin-left:220px!important;}' +
        '@media(max-width:640px){#masul-sidebar{display:none;}body{margin-left:0!important;}}';

    var styleEl = document.createElement('style');
    styleEl.textContent = css;
    document.head.appendChild(styleEl);
    document.body.insertAdjacentHTML('afterbegin', html);

    window.msbLogout = function () {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('current_user');
        window.location.href = '/';
    };
})();
