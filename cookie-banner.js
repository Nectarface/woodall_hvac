
    (function() {
        var banner = document.createElement('div');
        banner.id = 'cookie-banner';
        banner.innerHTML = `
            <div style="position: fixed; bottom: 20px; left: 20px; right: 20px; background: #0f172a; color: white; padding: 20px; border-radius: 15px; display: flex; justify-content: space-between; align-items: center; z-index: 9999; box-shadow: 0 10px 25px rgba(0,0,0,0.3); border: 1px solid #1e293b;">
                <p style="margin: 0; font-size: 14px; font-family: sans-serif;">We use cookies to improve your experience in Boone County. <a href="privacy.html" style="color: #3b82f6; text-decoration: underline;">Learn more</a></p>
                <button onclick="document.getElementById('cookie-banner').remove()" style="background: #3b82f6; color: white; border: none; padding: 8px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-left: 20px;">Accept</button>
            </div>
        `;
        document.body.appendChild(banner);
    })();
    