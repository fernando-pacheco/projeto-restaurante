/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: ["class"],
    content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
    theme: {
        extend: {
            borderRadius: {
                lg: "var(--radius)",
                md: "calc(var(--radius) - 2px)",
                sm: "calc(var(--radius) - 4px)",
            },
            colors: {
                salmon: {
                    '50': '#fdf5ef',
                    '100': '#fcede3',
                    '200': '#f6cab2',
                    '300': '#f0a781',
                    '400': '#e9794e',
                    '500': '#e3582c',
                    '600': '#d54021',
                    '700': '#b02f1e',
                    '800': '#8d281f',
                    '900': '#72231c',
                    '950': '#3d0f0d',
                },
                sidebar: {
                    DEFAULT: "hsl(var(--sidebar-background))",
                    foreground: "hsl(var(--sidebar-foreground))",
                    primary: "hsl(var(--sidebar-primary))",
                    "primary-foreground":
                        "hsl(var(--sidebar-primary-foreground))",
                    accent: "hsl(var(--sidebar-accent))",
                    "accent-foreground":
                        "hsl(var(--sidebar-accent-foreground))",
                    border: "hsl(var(--sidebar-border))",
                    ring: "hsl(var(--sidebar-ring))",
                },
            },
            fontFamily: {
                sans: "Inter",
            },
        },
    },
    plugins: [require("tailwindcss-animate")],
}
