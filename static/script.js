// Currency Switcher function
function switchCurrencies() {
    const form = document.querySelector(".conversion-form");
    const from = form.querySelector("select[name='from_currency']");
    const to = form.querySelector("select[name='to_currency']");

    // Swap values
    const temp = from.value;
    from.value = to.value;
    to.value = temp;

    // Submit form
    form.submit();
}

// Added to favorites function
document.addEventListener("DOMContentLoaded", function () {
    const favoriteForm = document.querySelector(".favorite-form");

    if (favoriteForm) {
        const button = favoriteForm.querySelector(".favorite-btn");
        const icon = favoriteForm.querySelector(".fav-heart-icon");
        const label = favoriteForm.querySelector(".fav-heart-label");

        button.addEventListener("click", async () => {
            const from_currency = favoriteForm.dataset.from;
            const to_currency = favoriteForm.dataset.to;

            try {
                const response = await fetch("/favorite", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ from_currency, to_currency })
                });

                const data = await response.json();

                if (data.success) {
                    // Toggle icon and label
                    if (data.added) {
                        icon.src = "static/images/heart-filled.svg";
                        label.textContent = "In Favorites";
                    } else if (data.removed) {
                        icon.src = "static/images/heart-empty.svg";
                        label.textContent = "Add to Favorites";
                    }
                }
            } catch (error) {
                console.error("Error updating favorite:", error);
            }
        });
    }
});

// Add the country flag in the select box
function applyPair(from, to) {
    const fromSelect = document.querySelector("select[name='from_currency']");
    const toSelect = document.querySelector("select[name='to_currency']");
    const amount = document.querySelector("input[name=amount]");

    fromSelect.value = from;
    toSelect.value = to;
    amount.value = 1;


    document.querySelector(".conversion-form").submit();
}
function setFlagBackground(select) {
    const selectedOption = select.options[select.selectedIndex];
    const flag = selectedOption.getAttribute('data-flag');
    if (flag) {
        // Assuming you use flagcdn or similar for flag images
        const flagUrl = `https://flagcdn.com/w80/${flag}.png`;
        select.style.backgroundImage = `url('${flagUrl}')`;
        select.classList.add('flag-bg');
        // For pseudo-element, set CSS variable
        select.style.setProperty('--flag-url', `url('${flagUrl}')`);
    } else {
        select.style.backgroundImage = '';
        select.classList.remove('flag-bg');
        select.style.removeProperty('--flag-url');
    }
}

// For pseudo-element background
document.querySelectorAll('.flag-select').forEach(select => {
    setFlagBackground(select);
    select.addEventListener('change', function() {
        setFlagBackground(this);
    });
});

// Remove from Favorites button
document.querySelectorAll('.remove-favorite-btn').forEach(btn => {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        const favPair = btn.closest('.fav-pair');
        const from = favPair.getAttribute('data-from');
        const to = favPair.getAttribute('data-to');

        fetch('/favorite', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ from_currency: from, to_currency: to })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success && data.removed) {
                favPair.remove();
            } else {
                alert('Could not remove favorite.');
            }
        });
    });
});


// Generating the HTML for the tech tools in about-mb.html
const tools = [
    {
        name: "HTML",
        image: "html.svg",
        desc: "HTML is the building block of all web pages. It was used to create and organize the content of each page on this website. With the help of Jinja2 (a tool that connects Python with HTML), we made the content dynamic — meaning it updates based on your actions and inputs.",
    },
    {
        name: "CSS",
        image: "css.svg",
        desc: "CSS was used to style the website, making it clean, modern, and easy to navigate. It helped shape the layout, colors, and animations that give the site its smooth, professional look.",
    },
    {
        name: "JavaScript",
        image: "js.svg",
        desc: "JavaScript added interactivity to the website. It powers features like the favorite button, the switch currency button, dynamic flag displays, and real-time updates without refreshing the page — all of which make your experience smoother and more responsive.",
    },
    {
        name: "Python (Flask)",
        image: "python.svg",
        desc: "Python is the main programming language behind the scenes, and Flask is the web framework that helped bring everything together. Flask handled user sessions, form submissions, routing between pages, and communication with the database and APIs — all while keeping the site lightweight and efficient.",
    },
    {
        name: "SQL",
        image: "sql.svg",
        desc: "SQL is the technology behind the scenes that stores and manages your data. We used it to save your login details, track your conversion history, and remember your favorite currency pairs. To save time and resources, the system can also reuse recent data instead of making new requests, especially when you convert the same pair within a short time."
    },
    {
        name: "API",
        image: "api.svg",
        desc: "The website connects to a real-time currency exchange API, which provides up-to-date exchange rates. This ensures you always get accurate and current conversion results without needing to refresh or leave the site."
    },
    {
        name: "JSON",
        image: "json.svg",
        desc: "JSON (JavaScript Object Notation) is the format used to receive and understand data from the exchange rate API. It helps the website read and process information like currency names, symbols, and rates in a lightweight and organized way."
    },
    {
        name: "Git & GitHub",
        image: "git.svg",
        desc: "Git is a version control tool that tracks all changes made during development. GitHub is where the project was hosted and backed up online. It allowed efficient teamwork, easy rollback if mistakes occurred, and smooth deployment of the final website."
    }
];


let toolsHTML = ``;

tools.forEach((tool) => {
    toolsHTML += `
    <div class="tool-card">
        <img src="../static/images/tools/${tool.image}" alt="${tool.name} Logo" class="tool-image">
        <div class="tool-content">
            <div>
                <h3 class="tool-title">${tool.name}</h3>
                <p>${tool.desc}</p>
            </div>
        </div>
    </div>
    `;
});

document.querySelector('.js-tools').innerHTML = toolsHTML;

// Generating the HTML for the language percentage in about-mb.html
const langs = [
    {
        name: "HTML",
        class: "html",
        percent: 31.1,
        image: "html.svg"
    },
    {
        name: "CSS",
        class: "css",
        percent: 35.8,
        image: "css.svg"
    },
    {
        name: "JavaScript",
        class: "js",
        percent: 7.5,
        image: "js.svg"
    },
    {
        name: "Python",
        class: "py",
        percent: 25.6,
        image: "python.svg"
    }
]

let langHTML = ``;

langs.forEach((lang) => {
    langHTML += `
    <div class="language-entry">
        <div class="label-row">
            <img class="lang-icon" src="../static/images/tools/${lang.image}" alt="${lang.name} Icon">
            ${lang.name} <span class="percent">${lang.percent}%</span>
        </div>
        <div class="language-bar-single">
            <div class="lang ${lang.class}" style="width: ${lang.percent}%;"></div>
        </div>
    </div>
    `
});

document.querySelector('.js-lang-usage').innerHTML = langHTML;


// Pop up function when deleting the account
function openDeleteModal() {
    document.getElementById("deleteAccountModal").style.display = "flex";
}

function closeDeleteModal() {
    document.getElementById("deleteAccountModal").style.display = "none";
}

