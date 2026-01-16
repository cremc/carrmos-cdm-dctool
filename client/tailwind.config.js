/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#197fe6",
                "background-light": "#f6f7f8",
                "background-dark": "#111921",
                "card-dark": "#1e293b",
                "border-dark": "#293038",
            },
            fontFamily: {
                "display": ["Inter", "sans-serif"],
                "body": ["Noto Sans", "sans-serif"],
            },
        },
    },
    plugins: [],
}
