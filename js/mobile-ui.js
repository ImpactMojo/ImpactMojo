        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            const navLinks = document.getElementById('navLinks');
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navContainer = document.querySelector('.nav-container');
            
            if (navLinks && navLinks.classList.contains('active')) {
                // Check if click is outside nav container
                if (navContainer && !navContainer.contains(e.target)) {
                    closeMobileMenu();
                }
            }
        });
        
        // Close mobile menu on scroll
        let lastScrollTop = 0;
        window.addEventListener('scroll', function() {
            const navLinks = document.getElementById('navLinks');
            
            if (navLinks && navLinks.classList.contains('active')) {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                // Close menu if scrolled more than 50px
                if (Math.abs(scrollTop - lastScrollTop) > 50) {
                    closeMobileMenu();
                }
            }
            lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
        }, { passive: true });

        // Mobile dropdown toggle (click to expand on mobile)
        document.addEventListener('DOMContentLoaded', function() {
            const dropdownItems = document.querySelectorAll('.nav-links > li.has-dropdown');
            
            dropdownItems.forEach(item => {
                const link = item.querySelector('a');
                link.addEventListener('click', function(e) {
                    // Only toggle on mobile (check if mobile menu toggle is visible)
                    const mobileToggle = document.querySelector('.mobile-menu-toggle');
                    if (mobileToggle && window.getComputedStyle(mobileToggle).display !== 'none') {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        // Close other dropdowns
                        dropdownItems.forEach(otherItem => {
                            if (otherItem !== item) {
                                otherItem.classList.remove('open');
                            }
                        });
                        
                        // Toggle this dropdown
                        item.classList.toggle('open');
                    }
                });
            });

            // Close dropdowns when clicking dropdown links on mobile
            const dropdownLinks = document.querySelectorAll('.dropdown-menu a');
            dropdownLinks.forEach(link => {
                link.addEventListener('click', function() {
                    const mobileToggle = document.querySelector('.mobile-menu-toggle');
                    if (mobileToggle && window.getComputedStyle(mobileToggle).display !== 'none') {
                        // Close the mobile menu after clicking a dropdown item
                        setTimeout(() => {
                            closeMobileMenu();
                        }, 100);
                    }
                });
            });
            
            // Close mobile menu when clicking non-dropdown nav links (like Home)
            const navDirectLinks = document.querySelectorAll('.nav-links > li:not(.has-dropdown) > a');
            navDirectLinks.forEach(link => {
                link.addEventListener('click', function() {
                    const mobileToggle = document.querySelector('.mobile-menu-toggle');
                    if (mobileToggle && window.getComputedStyle(mobileToggle).display !== 'none') {
                        setTimeout(() => {
                            closeMobileMenu();
                        }, 100);
                    }
                });
            });
        });

        // Modal functions
        function openModal(modalId) {
            document.getElementById(modalId).style.display = "block";
            
            // Load Google Calendar buttons when coaching modal opens
            if (modalId === 'coachingModal' && window.calendar && window.calendar.schedulingButton) {
                setTimeout(() => {
                    const bookingContainers = document.querySelectorAll('#coachingModal .booking-button-container');
                    bookingContainers.forEach((container) => {
                        if (!container.querySelector('button')) {
                            window.calendar.schedulingButton.load({
                                url: 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ2DlCV8HgdkAK-Oyzi9PhKJ45eKo6026Ix1nEEH8Vcx_lxfaCAZlzkcBvptD2sZm1P4fvHjU_Cq?gv=true',
                                color: '#039BE5',
                                label: 'Book an appointment',
                                target: container,
                            });
                        }
                    });
                }, 100);
            }
        }

        function closeModal(modalId) {
            document.getElementById(modalId).style.display = "none";
        }

        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target.classList.contains('modal')) {
                event.target.style.display = "none";
            }
        }

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Chatbot Functions
        let feedbackType = null;
        let currentStep = 'initial';
        let userRating = 0;
        let feedbackData = {};

        function openChatbot() {
            const modal = document.getElementById('chatbotModal');
            modal.classList.add('show');
            document.getElementById('chatInput').focus();
        }

        function closeChatbot() {
            const modal = document.getElementById('chatbotModal');
            modal.classList.remove('show');
            resetChat();
        }

        function resetChat() {
            feedbackType = null;
            currentStep = 'initial';
            userRating = 0;
            feedbackData = {};
        }

        function selectOption(type) {
            feedbackType = type;
            feedbackData.type = type;
            currentStep = 'collecting';
            
            const labels = {
                'feedback': 'General Feedback',
                'course': 'Suggest a Course',
                'bug': 'Report a Bug',
                'feature': 'Feature Request'
            };
            
            addUserMessage(labels[type]);
            
            setTimeout(() => {
                if (type === 'feedback') {
                    addBotMessage("Great! Let's start with a quick rating. How would you rate your overall experience?");
                    addStarRating();
                } else if (type === 'course') {
                    addBotMessage("Wonderful! What course topic would you like us to add? Please be as specific as possible.");
                } else if (type === 'bug') {
                    addBotMessage("Thank you for reporting! Please describe the issue and mention which page or feature it occurred on.");
                } else {
                    addBotMessage("Excellent! What feature would make ImpactMojo better for you?");
                }
            }, 500);
        }

        function addBotMessage(text) {
            const messages = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot-message';
            messageDiv.innerHTML = `
                <div class="bot-avatar">
                    <svg class="icon-sm" viewBox="0 0 24 24" style="stroke: white;">
                        <rect x="3" y="11" width="18" height="10" rx="2" ry="2"/>
                        <circle cx="12" cy="5" r="2"/>
                        <path d="M12 7v4"/>
                    </svg>
                </div>
                <div class="bot-bubble">${text}</div>
            `;
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }

        function addUserMessage(text) {
            const messages = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message user-message';
            messageDiv.innerHTML = `
                <div class="user-bubble">${text}</div>
            `;
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }

        function addStarRating() {
            const messages = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot-message';
            messageDiv.innerHTML = `
                <div class="bot-avatar">
                    <svg class="icon-sm" viewBox="0 0 24 24" style="stroke: white;">
                        <rect x="3" y="11" width="18" height="10" rx="2" ry="2"/>
                        <circle cx="12" cy="5" r="2"/>
                        <path d="M12 7v4"/>
                    </svg>
                </div>
                <div>
                    <div class="star-selector" style="display: flex; gap: 0.5rem; justify-content: center; padding: 1rem;">
                        <button class="star-btn" onclick="setRating(1)" style="cursor: pointer; background: none; border: none; padding: 4px;"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>
                        <button class="star-btn" onclick="setRating(2)" style="cursor: pointer; background: none; border: none; padding: 4px;"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>
                        <button class="star-btn" onclick="setRating(3)" style="cursor: pointer; background: none; border: none; padding: 4px;"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>
                        <button class="star-btn" onclick="setRating(4)" style="cursor: pointer; background: none; border: none; padding: 4px;"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>
                        <button class="star-btn" onclick="setRating(5)" style="cursor: pointer; background: none; border: none; padding: 4px;"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>
                    </div>
                </div>
            `;
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }

        function setRating(rating) {
            userRating = rating;
            feedbackData.rating = rating;
            
            // Update star display
            const stars = document.querySelectorAll('.star-btn');
            stars.forEach((star, index) => {
                if (index < rating) {
                    star.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24" fill="#FCD34D" stroke="#FCD34D" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>';
                    star.style.color = '#FCD34D';
                } else {
                    star.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#374151" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>';
                    star.style.color = '#374151';
                }
            });
            
            addUserMessage(`${rating} stars`);
            
            setTimeout(() => {
                addBotMessage("Thank you! Now, please share your detailed feedback:");
                currentStep = 'details';
            }, 500);
        }

        function sendMessage() {
            const input = document.getElementById('chatInput');
            const message = input.value.trim();
            
            if (!message) return;
            
            addUserMessage(message);
            input.value = '';
            
            if (currentStep === 'details' || currentStep === 'collecting') {
                feedbackData.message = message;
                currentStep = 'email';
                
                setTimeout(() => {
                    addBotMessage("Thank you for your feedback! Would you like to share your email so we can follow up? (Type 'skip' to skip)");
                }, 500);
            } else if (currentStep === 'email') {
                if (message.toLowerCase() !== 'skip') {
                    feedbackData.email = message;
                }
                submitFeedback();
            }
        }

        function submitFeedback() {
            // Show typing indicator
            addBotMessage('<div style="display: flex; gap: 4px;"><div style="width: 8px; height: 8px; background: var(--text-secondary); border-radius: 50%; animation: typing 1.4s infinite;"></div><div style="width: 8px; height: 8px; background: var(--text-secondary); border-radius: 50%; animation: typing 1.4s infinite; animation-delay: 0.2s;"></div><div style="width: 8px; height: 8px; background: var(--text-secondary); border-radius: 50%; animation: typing 1.4s infinite; animation-delay: 0.4s;"></div></div>');
            
            // Submit to Formspree
            fetch('https://formspree.io/f/xpwdvgzp', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(feedbackData)
            }).then(() => {
                // Remove typing indicator
                const messages = document.getElementById('chatMessages');
                messages.lastChild.remove();
                
                addBotMessage("Your feedback has been submitted successfully! Thank you for helping us improve ImpactMojo.");
                
                setTimeout(() => {
                    addBotMessage("Feel free to close this chat or share more feedback anytime!");
                }, 1500);
                
                currentStep = 'complete';
            });
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }


        // Track quiz configuration
        const TRACK_CONFIG = {
            data: {
                name: 'Data & Technology Track',
                anchor: '/handouts#data-technology',
                summary: 'Start with econometrics, data visualization, and AI tools for development data.'
            },
            gender: {
                name: 'Gender, Equity & Inclusion Track',
                anchor: '/handouts#gender-equity-inclusion',
                summary: 'Explore gender, caste, intersectionality, and structural inequality in development practice.'
            },
            policy: {
                name: 'Policy & Economics Track',
                anchor: '/handouts#policy-economics',
                summary: 'Understand growth, inequality, political economy, and public finance for better decisions.'
            },
            methods: {
                name: 'Monitoring, Evaluation & Learning Track',
                anchor: '/handouts#monitoring-evaluation-learning',
                summary: 'Strengthen MEL frameworks, TOC design, qualitative methods, and research ethics.'
            },
            philosophy: {
                name: 'Philosophy, Law & Governance Track',
                anchor: '/handouts#philosophy-law-governance',
                summary: 'Ground your practice in Gandhian thought, constitutional law, and governance frameworks.'
            },
            health: {
                name: 'Health, Communication & Wellbeing Track',
                anchor: '/handouts#health-communication-wellbeing',
                summary: 'Build skills in public health, SRHR, BCC, storytelling, and social-emotional learning.'
            }
        };

        function saveTrackQuiz(event) {
            event.preventDefault();
            const form = event.target;
            const checked = form.querySelectorAll('input[type="radio"]:checked');

            const scores = { data: 0, gender: 0, policy: 0, methods: 0, philosophy: 0, health: 0 };
            checked.forEach(input => {
                const trackKey = input.getAttribute('data-track');
                if (trackKey && scores[trackKey] !== undefined) {
                    scores[trackKey]++;
                }
            });

            // Persist a lightweight copy in localStorage (for future analytics)
            try {
                const answers = {};
                checked.forEach(input => {
                    answers[input.name] = input.value;
                });
                const existing = JSON.parse(localStorage.getItem('impactmojoTrackQuiz') || '[]');
                existing.push({
                    timestamp: new Date().toISOString(),
                    ...answers
                });
                localStorage.setItem('impactmojoTrackQuiz', JSON.stringify(existing.slice(-20)));
            } catch (e) {
                console.warn('Could not save quiz responses', e);
            }

            // Compute best track
            let bestTrack = 'data';
            let bestScore = -1;
            Object.keys(scores).forEach(key => {
                if (scores[key] > bestScore) {
                    bestScore = scores[key];
                    bestTrack = key;
                }
            });

            const config = TRACK_CONFIG[bestTrack];
            const resultBox = document.getElementById('trackQuizResult');
            const resultText = document.getElementById('trackQuizResultText');
            const resultLink = document.getElementById('trackQuizResultLink');

            if (config && resultBox && resultText && resultLink) {
                resultText.textContent = config.summary;
                resultLink.innerHTML = 'Recommended starting point: <a href="' + config.anchor + '">'
                    + config.name + '</a>';
                resultBox.style.display = 'block';
                resultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        // Ensure a fresh view when returning via back/forward cache
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                window.location.reload();
            }
        });

        // ========================================
        // VERSION CHECK & AUTO-REFRESH
        // ========================================
        (function() {
            var SITE_VERSION = '9.10.0.20260128'; // Update this when deploying new versions - Jan 28 2026: Dojos, light mode default, design fixes
            var VERSION_KEY = 'imx_site_version';
            
            // Check if version changed
            var storedVersion = localStorage.getItem(VERSION_KEY);
            if (storedVersion && storedVersion !== SITE_VERSION) {
                localStorage.setItem(VERSION_KEY, SITE_VERSION);
                // Clear any cached data that might cause issues
                if ('caches' in window) {
                    caches.keys().then(function(names) {
                        names.forEach(function(name) {
                            caches.delete(name);
                        });
                    });
                }
                window.location.reload(true); // Force reload from server
            } else {
                localStorage.setItem(VERSION_KEY, SITE_VERSION);
            }
            
            // Also check for updates periodically (every 30 minutes)
            setInterval(function() {
                fetch(window.location.href + '?_=' + Date.now(), { 
                    method: 'HEAD',
                    cache: 'no-store'
                }).then(function(response) {
                    var lastModified = response.headers.get('last-modified');
                    var storedLastMod = sessionStorage.getItem('imx_last_modified');
                    if (storedLastMod && lastModified && storedLastMod !== lastModified) {
                        if (confirm('A new version of ImpactMojo is available! Refresh now?')) {
                            window.location.reload(true);
                        }
                    }
                    if (lastModified) {
                        sessionStorage.setItem('imx_last_modified', lastModified);
                    }
                }).catch(function() {});
            }, 30 * 60 * 1000); // 30 minutes
        })();

        // Service Worker - DISABLED for now to fix caching issues
        // Unregister any existing service workers to ensure fresh content
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.getRegistrations().then(function(registrations) {
                for (let registration of registrations) {
                    registration.unregister().then(function() {
                    });
                }
            });
            // Clear all caches
            if ('caches' in window) {
                caches.keys().then(function(names) {
                    names.forEach(function(name) {
                        caches.delete(name);
                    });
                });
            }
        }
        // Original SW registration - COMMENTED OUT
        // if ('serviceWorker' in navigator) {
        //     window.addEventListener('load', () => {
        //         navigator.serviceWorker.register('service-worker.js')
        //             .then(registration => console.log('ServiceWorker registration successful'))
        //             .catch(err => console.log('ServiceWorker registration failed: ', err));
        //     });
        // }
