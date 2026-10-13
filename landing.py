<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | InnovateX</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            500: '#0284c7',
                            600: '#0284c7',
                            700: '#0369a1',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            transition: background-color 0.3s, color 0.3s;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-slate-900 dark:text-slate-100 transition-colors duration-300">

    <!-- Navigation Bar -->
    <nav class="fixed w-full z-50 top-0 left-0 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-white font-bold text-xl shadow-md">
                        X
                    </div>
                    <span class="text-xl font-bold bg-gradient-to-r from-sky-600 to-indigo-600 bg-clip-text text-transparent">
                        InnovateX
                    </span>
                </div>

                <!-- Desktop Menu -->
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium">
                    <a href="#hero" class="hover:text-sky-500 transition-colors">Home</a>
                    <a href="#about" class="hover:text-sky-500 transition-colors">About</a>
                    <a href="#values" class="hover:text-sky-500 transition-colors">Values</a>
                    <a href="#team" class="hover:text-sky-500 transition-colors">Team</a>
                    <a href="#contact" class="hover:text-sky-500 transition-colors">Contact</a>
                </div>

                <!-- Dark Mode Toggle & Mobile Menu Btn -->
                <div class="flex items-center space-x-4">
                    <button id="themeToggle" class="p-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all duration-200">
                        <i id="themeIcon" class="fa-solid fa-moon text-lg"></i>
                    </button>

                    <button id="mobileMenuBtn" class="md:hidden p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">
                        <i class="fa-solid fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobileMenu" class="hidden md:hidden border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 px-4 pt-2 pb-4 space-y-2 text-sm font-medium">
            <a href="#hero" class="block py-2 hover:text-sky-500">Home</a>
            <a href="#about" class="block py-2 hover:text-sky-500">About</a>
            <a href="#values" class="block py-2 hover:text-sky-500">Values</a>
            <a href="#team" class="block py-2 hover:text-sky-500">Team</a>
            <a href="#contact" class="block py-2 hover:text-sky-500">Contact</a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="hero" class="pt-32 pb-20 md:pt-40 md:pb-28 relative overflow-hidden">
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-sky-400/20 dark:bg-sky-500/10 rounded-full blur-3xl -z-10"></div>
        <div class="absolute top-60 -left-40 w-96 h-96 bg-indigo-400/20 dark:bg-indigo-500/10 rounded-full blur-3xl -z-10"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <span class="px-4 py-1.5 rounded-full text-xs font-semibold uppercase tracking-wider bg-sky-100 dark:bg-sky-900/50 text-sky-600 dark:text-sky-300 inline-block mb-4">
                Pioneering The Future
            </span>
            <h1 class="text-4xl sm:text-6xl font-extrabold tracking-tight mb-6">
                We Build Digital Tools That <br class="hidden sm:inline">
                <span class="bg-gradient-to-r from-sky-500 to-indigo-600 bg-clip-text text-transparent">Empower Tomorrow</span>
            </h1>
            <p class="max-w-2xl mx-auto text-lg text-slate-600 dark:text-slate-400 mb-8 leading-relaxed">
                We are a collective of visionaries, engineers, and designers passionate about creating seamless software solutions that elevate businesses and enrich lives.
            </p>
            <div class="flex justify-center gap-4">
                <a href="#about" class="px-6 py-3 rounded-xl bg-sky-600 hover:bg-sky-700 text-white font-medium shadow-lg shadow-sky-500/25 transition-all transform hover:-translate-y-0.5">
                    Our Story
                </a>
                <a href="#contact" class="px-6 py-3 rounded-xl bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 font-medium transition-all">
                    Get in Touch
                </a>
            </div>
        </div>
    </section>

    <!-- About Us Detailed Section -->
    <section id="about" class="py-20 bg-white dark:bg-slate-800/50 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div class="space-y-6">
                    <h2 class="text-3xl sm:text-4xl font-bold tracking-tight">
                        Driven by Curiosity, Grounded in Excellence
                    </h2>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed">
                        Founded in 2021, InnovateX started with a simple belief: code should solve real-world problems with elegance and efficiency. What began as a small group of enthusiastic engineers has evolved into an international team delivering high-impact web and mobile products.
                    </p>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed">
                        Our workflow combines rigorous architectural design with rapid iterative deployment. We bridge the gap between complex backend infrastructure and delightful user interfaces.
                    </p>
                    
                    <!-- Stats Grid -->
                    <div class="grid grid-cols-3 gap-4 pt-4 border-t border-slate-200 dark:border-slate-700">
                        <div>
                            <p class="text-3xl font-extrabold text-sky-600 dark:text-sky-400">150+</p>
                            <p class="text-sm text-slate-500 dark:text-slate-400">Projects Built</p>
                        </div>
                        <div>
                            <p class="text-3xl font-extrabold text-sky-600 dark:text-sky-400">99.9%</p>
                            <p class="text-sm text-slate-500 dark:text-slate-400">Uptime Rate</p>
                        </div>
                        <div>
                            <p class="text-3xl font-extrabold text-sky-600 dark:text-sky-400">15+</p>
                            <p class="text-sm text-slate-500 dark:text-slate-400">Global Awards</p>
                        </div>
                    </div>
                </div>

                <!-- Graphic/Image Container -->
                <div class="relative">
                    <div class="w-full h-80 sm:h-96 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 p-1 shadow-2xl">
                        <div class="w-full h-full bg-slate-900 rounded-[14px] flex items-center justify-center relative overflow-hidden">
                            <div class="text-center p-8 space-y-4">
                                <i class="fa-solid fa-laptop-code text-6xl text-sky-400"></i>
                                <h3 class="text-xl font-bold text-white">Crafting Code with Purpose</h3>
                                <p class="text-slate-400 text-sm max-w-sm">Combining modern stack capabilities with clean UI/UX standards.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Mission, Vision & Values -->
    <section id="values" class="py-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <h2 class="text-3xl sm:text-4xl font-bold mb-4">What Guides Us</h2>
                <p class="text-slate-600 dark:text-slate-400">Our core values define how we collaborate, innovate, and deliver value for our community.</p>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <!-- Card 1: Mission -->
                <div class="p-8 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/60 shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-sky-100 dark:bg-sky-900/50 text-sky-600 dark:text-sky-400 flex items-center justify-center text-xl mb-6">
                        <i class="fa-solid fa-bullseye"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Our Mission</h3>
                    <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">
                        To simplify complex workflows by providing intuitive, high-performance web applications that empower individuals and organizations worldwide.
                    </p>
                </div>

                <!-- Card 2: Vision -->
                <div class="p-8 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/60 shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-indigo-100 dark:bg-indigo-900/50 text-indigo-600 dark:text-indigo-400 flex items-center justify-center text-xl mb-6">
                        <i class="fa-solid fa-eye"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Our Vision</h3>
                    <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">
                        To become a benchmark for modern web development standards, recognized for developer experience, software security, and user accessibility.
                    </p>
                </div>

                <!-- Card 3: Values -->
                <div class="p-8 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/60 shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-emerald-100 dark:bg-emerald-900/50 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xl mb-6">
                        <i class="fa-solid fa-heart"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Core Values</h3>
                    <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">
                        Transparency, continuous learning, robust craftsmanship, and empathy in design guide every single pull request we create.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="py-20 bg-white dark:bg-slate-800/50 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <h2 class="text-3xl sm:text-4xl font-bold mb-4">Meet the Team</h2>
                <p class="text-slate-600 dark:text-slate-400">The talented minds behind our products.</p>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Team Member 1 -->
                <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center group hover:shadow-lg transition-all">
                    <div class="w-24 h-24 mx-auto mb-4 rounded-full bg-gradient-to-tr from-sky-400 to-indigo-500 p-1">
                        <img src="https://placehold.co/200x200/0284c7/ffffff?text=AS" alt="Alex Smith" class="w-full h-full object-cover rounded-full">
                    </div>
                    <h3 class="font-bold text-lg">Alex Smith</h3>
                    <p class="text-sky-600 dark:text-sky-400 text-sm font-medium mb-3">Founder & Lead Architect</p>
                    <p class="text-slate-500 dark:text-slate-400 text-xs leading-relaxed mb-4">Passionate about scalable web architectures and developer tools.</p>
                    <div class="flex justify-center space-x-3 text-slate-400">
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-github"></i></a>
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-x-twitter"></i></a>
                    </div>
                </div>

                <!-- Team Member 2 -->
                <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center group hover:shadow-lg transition-all">
                    <div class="w-24 h-24 mx-auto mb-4 rounded-full bg-gradient-to-tr from-sky-400 to-indigo-500 p-1">
                        <img src="https://placehold.co/200x200/4f46e5/ffffff?text=SL" alt="Sarah Lee" class="w-full h-full object-cover rounded-full">
                    </div>
                    <h3 class="font-bold text-lg">Sarah Lee</h3>
                    <p class="text-sky-600 dark:text-sky-400 text-sm font-medium mb-3">Head of UI/UX Design</p>
                    <p class="text-slate-500 dark:text-slate-400 text-xs leading-relaxed mb-4">Crafting accessible, aesthetically pleasing digital experiences.</p>
                    <div class="flex justify-center space-x-3 text-slate-400">
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-github"></i></a>
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-dribbble"></i></a>
                    </div>
                </div>

                <!-- Team Member 3 -->
                <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center group hover:shadow-lg transition-all sm:col-span-2 lg:col-span-1">
                    <div class="w-24 h-24 mx-auto mb-4 rounded-full bg-gradient-to-tr from-sky-400 to-indigo-500 p-1">
                        <img src="https://placehold.co/200x200/10b981/ffffff?text=MJ" alt="Michael Johnson" class="w-full h-full object-cover rounded-full">
                    </div>
                    <h3 class="font-bold text-lg">Michael Johnson</h3>
                    <p class="text-sky-600 dark:text-sky-400 text-sm font-medium mb-3">Senior DevOps Engineer</p>
                    <p class="text-slate-500 dark:text-slate-400 text-xs leading-relaxed mb-4">Automating deployment pipelines and ensuring 99.9% system availability.</p>
                    <div class="flex justify-center space-x-3 text-slate-400">
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-github"></i></a>
                        <a href="#" class="hover:text-sky-500 transition-colors"><i class="fa-brands fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer id="contact" class="border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Col 1 -->
                <div class="md:col-span-2 space-y-4">
                    <div class="flex items-center space-x-3">
                        <div class="w-8 h-8 rounded-lg bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-white font-bold text-lg">
                            X
                        </div>
                        <span class="text-lg font-bold">InnovateX</span>
                    </div>
                    <p class="text-slate-500 dark:text-slate-400 text-sm max-w-sm">
                        Building high-performance modern web solutions for the digital age.
                    </p>
                </div>

                <!-- Col 2 -->
                <div>
                    <h4 class="font-semibold text-sm uppercase tracking-wider mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-sm text-slate-500 dark:text-slate-400">
                        <li><a href="#about" class="hover:text-sky-500">About Us</a></li>
                        <li><a href="#values" class="hover:text-sky-500">Core Values</a></li>
                        <li><a href="#team" class="hover:text-sky-500">Team</a></li>
                    </ul>
                </div>

                <!-- Col 3 -->
                <div>
                    <h4 class="font-semibold text-sm uppercase tracking-wider mb-4">Contact</h4>
                    <p class="text-sm text-slate-500 dark:text-slate-400 mb-2"><i class="fa-regular fa-envelope mr-2"></i>contact@innovatex.io</p>
                    <p class="text-sm text-slate-500 dark:text-slate-400"><i class="fa-solid fa-location-dot mr-2"></i>Global Remote Team</p>
                </div>
            </div>

            <div class="mt-12 pt-6 border-t border-slate-100 dark:border-slate-800 flex flex-col sm:flex-row justify-between items-center text-xs text-slate-400">
                <p>&copy; 2026 InnovateX. All rights reserved.</p>
                <div class="flex space-x-4 mt-4 sm:mt-0">
                    <a href="#" class="hover:text-sky-500">Privacy Policy</a>
                    <a href="#" class="hover:text-sky-500">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Interactive Logic Script -->
    <script>
        // Dark Mode Logic
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const html = document.documentElement;

        // Check system preference or saved theme
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            html.classList.add('dark');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        } else {
            html.classList.remove('dark');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
        }

        themeToggle.addEventListener('click', () => {
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.theme = 'light';
                themeIcon.classList.replace('fa-sun', 'fa-moon');
            } else {
                html.classList.add('dark');
                localStorage.theme = 'dark';
                themeIcon.classList.replace('fa-moon', 'fa-sun');
            }
        });

        // Mobile Menu Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const mobileMenu = document.getElementById('mobileMenu');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    </script>
</body>
</html>
