import tkinter as tk
from tkinter import messagebox
import math
import random
from tkinter import font

class UltraModernTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎮 AI Mode Tic-Tac-Toe")
        
        # Get screen dimensions for responsive design
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # Set window to 80% of screen size
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.85)
        
        # Center window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.configure(bg='#0a0a0a')
        self.window.resizable(True, True)
        self.window.minsize(800, 600)
        
        # Ultra modern color palette
        self.colors = {
            'bg_primary': '#0a0a0a',          # Deep black
            'bg_secondary': '#1a1a2e',        # Dark navy
            'bg_tertiary': '#2d3748',         # Lighter gray for better contrast
            'accent_primary': '#6c5ce7',      # Purple
            'accent_secondary': '#a29bfe',    # Light purple
            'accent_tertiary': '#fd79a8',     # Pink
            'success': '#00b894',             # Teal green
            'warning': '#fdcb6e',             # Orange
            'danger': '#e84393',              # Pink red
            'info': '#74b9ff',                # Blue
            'text_primary': '#ffffff',        # Pure white
            'text_secondary': '#e2e8f0',      # Light gray for better readability
            'text_muted': '#a0aec0',          # Muted gray
            'border': '#4a5568',              # Visible border
            'shadow': '#00000050',            # Semi-transparent black
            'x_gradient_start': '#ff6b6b',    # Red start
            'x_gradient_end': '#ee5a52',      # Red end
            'o_gradient_start': '#4ecdc4',    # Cyan start
            'o_gradient_end': '#44a08d',      # Cyan end
            'board_bg': '#2d3748',            # Better board background
            'button_hover': '#4a5568',        # Visible hover effect
            'win_glow': '#ffd700',            # Golden win highlight
            'grid_line': '#6c5ce7'            # Purple grid lines
        }
        
        # Game state
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_mode = None
        self.game_active = False
        self.difficulty = 'hard'
        self.scores = {'player': 0, 'opponent': 0, 'draw': 0}
        self.game_count = 0
        
        # Animation variables
        self.hover_animation = {}
        self.pulse_animation = False
        
        self.setup_fonts()
        self.setup_ultra_modern_ui()
        
    def setup_fonts(self):
        """Setup modern fonts"""
        try:
            self.fonts = {
                'title': ('Segoe UI Light', 36, 'normal'),
                'subtitle': ('Segoe UI', 14, 'normal'),
                'heading': ('Segoe UI Semibold', 18, 'bold'),
                'body': ('Segoe UI', 12, 'normal'),
                'button': ('Segoe UI Semibold', 11, 'bold'),
                'board': ('Segoe UI Black', 48, 'bold'),
                'stats': ('Segoe UI', 13, 'normal'),
                'small': ('Segoe UI', 10, 'normal')
            }
        except:
            # Fallback fonts
            self.fonts = {
                'title': ('Arial', 32, 'normal'),
                'subtitle': ('Arial', 12, 'normal'),
                'heading': ('Arial', 16, 'bold'),
                'body': ('Arial', 11, 'normal'),
                'button': ('Arial', 10, 'bold'),
                'board': ('Arial', 42, 'bold'),
                'stats': ('Arial', 11, 'normal'),
                'small': ('Arial', 9, 'normal')
            }
    
    def setup_ultra_modern_ui(self):
        """Setup ultra modern UI with advanced styling"""
        # Main container with padding
        main_container = tk.Frame(self.window, bg=self.colors['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Top header section
        self.create_header_section(main_container)
        
        # Main content area
        content_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        content_frame.pack(fill='both', expand=True, pady=20)
        
        # Create three-column layout
        self.create_three_column_layout(content_frame)
        
        # Bottom status bar
        self.create_status_bar(main_container)
        
        # Start pulse animation for accent elements
        self.start_pulse_animation()
    
    def create_header_section(self, parent):
        """Create stunning header with gradient effect"""
        header_container = tk.Frame(parent, bg=self.colors['bg_primary'], height=120)
        header_container.pack(fill='x', pady=(0, 20))
        header_container.pack_propagate(False)
        
        # Header background with simulated gradient
        header_bg = tk.Frame(header_container, bg=self.colors['bg_secondary'], relief='flat')
        header_bg.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Title section
        title_frame = tk.Frame(header_bg, bg=self.colors['bg_secondary'])
        title_frame.pack(expand=True)
        
        # Main title with modern styling
        title_label = tk.Label(
            title_frame,
            text="🎮 AI MODED TIC-TAC-TOE",
            font=self.fonts['title'],
            fg=self.colors['accent_primary'],
            bg=self.colors['bg_secondary']
        )
        title_label.pack(pady=(15, 0))
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="TIC-TAC-TOE",
            font=self.fonts['heading'],
            fg=self.colors['text_primary'],
            bg=self.colors['bg_secondary']
        )
        subtitle_label.pack()
        
        # Tagline
        tagline_label = tk.Label(
            title_frame,
            text="Experience the future of classic gaming",
            font=self.fonts['subtitle'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_secondary']
        )
        tagline_label.pack(pady=(5, 15))
    
    def create_three_column_layout(self, parent):
        """Create three-column layout with modern panels"""
        # Left panel - Game controls
        left_panel = tk.Frame(parent, bg=self.colors['bg_secondary'], width=280)
        left_panel.pack(side='left', fill='y', padx=(0, 15))
        left_panel.pack_propagate(False)
        
        # Center panel - Game board
        center_panel = tk.Frame(parent, bg=self.colors['bg_primary'])
        center_panel.pack(side='left', fill='both', expand=True, padx=15)
        
        # Right panel - Statistics and info
        right_panel = tk.Frame(parent, bg=self.colors['bg_secondary'], width=280)
        right_panel.pack(side='right', fill='y', padx=(15, 0))
        right_panel.pack_propagate(False)
        
        self.setup_left_panel(left_panel)
        self.setup_center_panel(center_panel)
        self.setup_right_panel(right_panel)
    
    def setup_left_panel(self, panel):
        """Setup advanced left control panel"""
        # Panel header
        header_frame = tk.Frame(panel, bg=self.colors['bg_tertiary'], height=50)
        header_frame.pack(fill='x', padx=15, pady=15)
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame,
            text="🎯 GAME CONTROLS",
            font=self.fonts['heading'],
            fg=self.colors['text_primary'],
            bg=self.colors['bg_tertiary']
        )
        header_label.pack(expand=True)
        
        # Game mode selection
        mode_section = self.create_section(panel, "Select Game Mode")
        
        self.create_gradient_button(
            mode_section, 
            "🤖 AI CHALLENGE",
            lambda: self.select_mode('ai'),
            self.colors['accent_primary'],
            self.colors['accent_secondary']
        )
        
        self.create_gradient_button(
            mode_section,
            "👥 FRIEND BATTLE", 
            lambda: self.select_mode('human'),
            self.colors['success'],
            self.colors['info']
        )
        
        # AI difficulty section
        self.difficulty_section = self.create_section(panel, "AI Difficulty Level")
        
        self.difficulty_buttons = {}
        difficulties = [
            ('easy', '😊 BEGINNER', self.colors['success'], self.colors['info']),
            ('medium', '😐 INTERMEDIATE', self.colors['warning'], self.colors['accent_tertiary']),
            ('hard', '😤 EXPERT', self.colors['danger'], self.colors['accent_primary'])
        ]
        
        for diff, text, color1, color2 in difficulties:
            btn = self.create_difficulty_button(self.difficulty_section, text, diff, color1, color2)
            self.difficulty_buttons[diff] = btn
        
        # Game controls
        controls_section = self.create_section(panel, "Game Actions")
        
        self.create_gradient_button(
            controls_section,
            "🔄 NEW GAME",
            self.reset_game,
            self.colors['warning'],
            self.colors['accent_tertiary']
        )
        
        self.create_gradient_button(
            controls_section,
            "📊 RESET STATS",
            self.reset_scores,
            self.colors['danger'],
            self.colors['accent_primary']
        )
        
        self.create_gradient_button(
            controls_section,
            "❌ EXIT GAME",
            self.window.quit,
            self.colors['text_muted'],
            self.colors['border']
        )
    
    def create_section(self, parent, title):
        """Create a styled section"""
        section_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        section_frame.pack(fill='x', padx=15, pady=10)
        
        # Section title
        title_label = tk.Label(
            section_frame,
            text=title,
            font=self.fonts['body'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_secondary']
        )
        title_label.pack(anchor='w', pady=(0, 8))
        
        return section_frame
    
    def create_gradient_button(self, parent, text, command, color1, color2):
        """Create gradient-style button"""
        # Create button frame for gradient effect
        button_frame = tk.Frame(parent, bg=color1, relief='flat', bd=0)
        button_frame.pack(fill='x', pady=3)
        
        button = tk.Button(
            button_frame,
            text=text,
            font=self.fonts['button'],
            bg=color1,
            fg=self.colors['text_primary'],
            relief='flat',
            bd=0,
            padx=20,
            pady=12,
            command=command,
            cursor='hand2',
            activebackground=color2,
            activeforeground=self.colors['text_primary']
        )
        button.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Add hover animations
        button.bind("<Enter>", lambda e: self.on_button_enter(button, color2))
        button.bind("<Leave>", lambda e: self.on_button_leave(button, color1))
        
        return button
    
    def create_difficulty_button(self, parent, text, difficulty, color1, color2):
        """Create difficulty selection button"""
        is_selected = self.difficulty == difficulty
        current_color = color1 if is_selected else self.colors['bg_tertiary']
        
        button_frame = tk.Frame(parent, bg=current_color, relief='flat')
        button_frame.pack(fill='x', pady=2)
        
        button = tk.Button(
            button_frame,
            text=text,
            font=self.fonts['small'],
            bg=current_color,
            fg=self.colors['text_primary'],
            relief='flat',
            bd=0,
            padx=15,
            pady=8,
            command=lambda: self.set_difficulty(difficulty),
            cursor='hand2'
        )
        button.pack(fill='both', expand=True, padx=1, pady=1)
        
        return button
    
    def setup_center_panel(self, panel):
        """Setup center game board with enhanced modern styling"""
        # Game status section
        status_frame = tk.Frame(panel, bg=self.colors['bg_primary'])
        status_frame.pack(pady=(0, 20))
        
        self.status_label = tk.Label(
            status_frame,
            text="Select a game mode to begin your journey",
            font=self.fonts['heading'],
            fg=self.colors['text_primary'],
            bg=self.colors['bg_primary']
        )
        self.status_label.pack()
        
        # Current turn indicator
        self.turn_indicator = tk.Label(
            status_frame,
            text="",
            font=self.fonts['body'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_primary']
        )
        self.turn_indicator.pack(pady=(5, 0))
        
        # Game board container with proper centering
        board_container = tk.Frame(panel, bg=self.colors['bg_primary'])
        board_container.pack(expand=True, fill='both')
        
        # Center frame to properly center the board
        center_frame = tk.Frame(board_container, bg=self.colors['bg_primary'])
        center_frame.pack(expand=True)
        
        # Board outer frame with enhanced styling
        board_outer_frame = tk.Frame(
            center_frame,
            bg=self.colors['accent_primary'],
            relief='flat',
            bd=0
        )
        board_outer_frame.pack(pady=30)
        
        # Board inner frame with grid background
        self.board_frame = tk.Frame(
            board_outer_frame,
            bg=self.colors['bg_secondary'],
            relief='flat',
            bd=0
        )
        self.board_frame.pack(padx=6, pady=6)
        
        # Create enhanced game grid with better visibility
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            
            # Create button with fixed size and enhanced styling
            button = tk.Button(
                self.board_frame,
                text='',
                font=self.fonts['board'],
                width=4, height=2,
                bg=self.colors['bg_tertiary'],
                fg=self.colors['text_primary'],
                command=lambda pos=i: self.make_move(pos),
                cursor='hand2',
                state='disabled',
                relief='flat',
                bd=0,
                activebackground=self.colors['button_hover']
            )
            button.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')
            self.buttons.append(button)
            
            # Configure grid weights for proper sizing
            self.board_frame.grid_rowconfigure(row, weight=1)
            self.board_frame.grid_columnconfigure(col, weight=1)
            
            # Enhanced hover effects
            button.bind("<Enter>", lambda e, btn=button, pos=i: self.on_board_hover_enter(btn, pos))
            button.bind("<Leave>", lambda e, btn=button, pos=i: self.on_board_hover_leave(btn, pos))
        
        # Add board size constraints
        self.board_frame.configure(width=300, height=300)
        self.board_frame.pack_propagate(False)
    
    def setup_right_panel(self, panel):
        """Setup right statistics panel"""
        # Panel header
        header_frame = tk.Frame(panel, bg=self.colors['bg_tertiary'], height=50)
        header_frame.pack(fill='x', padx=15, pady=15)
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame,
            text="📊 GAME ANALYTICS",
            font=self.fonts['heading'],
            fg=self.colors['text_primary'],
            bg=self.colors['bg_tertiary']
        )
        header_label.pack(expand=True)
        
        # Current game info
        current_section = self.create_section(panel, "Current Session")
        
        self.current_info_frame = tk.Frame(current_section, bg=self.colors['bg_tertiary'])
        self.current_info_frame.pack(fill='x', pady=5)
        
        self.current_mode_label = tk.Label(
            self.current_info_frame,
            text="Mode: Not Selected",
            font=self.fonts['stats'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_tertiary']
        )
        self.current_mode_label.pack(anchor='w', padx=10, pady=2)
        
        self.current_difficulty_label = tk.Label(
            self.current_info_frame,
            text="Difficulty: Expert",
            font=self.fonts['stats'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_tertiary']
        )
        self.current_difficulty_label.pack(anchor='w', padx=10, pady=2)
        
        self.games_played_label = tk.Label(
            self.current_info_frame,
            text="Games Played: 0",
            font=self.fonts['stats'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_tertiary']
        )
        self.games_played_label.pack(anchor='w', padx=10, pady=2)
        
        # Statistics section
        stats_section = self.create_section(panel, "Performance Metrics")
        
        self.stats_frame = tk.Frame(stats_section, bg=self.colors['bg_tertiary'])
        self.stats_frame.pack(fill='x', pady=5)
        
        # Score displays
        self.wins_label = tk.Label(
            self.stats_frame,
            text="🏆 Wins: 0",
            font=self.fonts['stats'],
            fg=self.colors['success'],
            bg=self.colors['bg_tertiary']
        )
        self.wins_label.pack(anchor='w', padx=10, pady=2)
        
        self.losses_label = tk.Label(
            self.stats_frame,
            text="💀 Losses: 0",
            font=self.fonts['stats'],
            fg=self.colors['danger'],
            bg=self.colors['bg_tertiary']
        )
        self.losses_label.pack(anchor='w', padx=10, pady=2)
        
        self.draws_label = tk.Label(
            self.stats_frame,
            text="🤝 Draws: 0",
            font=self.fonts['stats'],
            fg=self.colors['warning'],
            bg=self.colors['bg_tertiary']
        )
        self.draws_label.pack(anchor='w', padx=10, pady=2)
        
        # Win rate
        self.winrate_label = tk.Label(
            self.stats_frame,
            text="📈 Win Rate: 0%",
            font=self.fonts['stats'],
            fg=self.colors['accent_primary'],
            bg=self.colors['bg_tertiary']
        )
        self.winrate_label.pack(anchor='w', padx=10, pady=2)
        
        # Strategy tips
        tips_section = self.create_section(panel, "Pro Strategies")
        
        tips_frame = tk.Frame(tips_section, bg=self.colors['bg_tertiary'])
        tips_frame.pack(fill='x', pady=5)
        
        tips_text = [
            "💡 Control the center square",
            "🎯 Secure corner positions", 
            "🛡️ Block opponent threats",
            "⚡ Create double threats",
            "🧠 Think 2 moves ahead"
        ]
        
        for tip in tips_text:
            tip_label = tk.Label(
                tips_frame,
                text=tip,
                font=self.fonts['small'],
                fg=self.colors['text_secondary'],
                bg=self.colors['bg_tertiary'],
                anchor='w'
            )
            tip_label.pack(fill='x', padx=10, pady=1)
    
    def create_status_bar(self, parent):
        """Create modern status bar"""
        status_bar = tk.Frame(parent, bg=self.colors['bg_secondary'], height=40)
        status_bar.pack(fill='x', pady=(20, 0))
        status_bar.pack_propagate(False)
        
        # Left side - game info
        left_status = tk.Label(
            status_bar,
            text="Ready to play • Ultra Modern Tic-Tac-Toe v2.0",
            font=self.fonts['small'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_secondary']
        )
        left_status.pack(side='left', padx=15, pady=10)
        
        # Right side - credits
        right_status = tk.Label(
            status_bar,
            text="Created with ❤️ using Python & Advanced Tkinter",
            font=self.fonts['small'],
            fg=self.colors['text_muted'],
            bg=self.colors['bg_secondary']
        )
        right_status.pack(side='right', padx=15, pady=10)
    
    def on_button_enter(self, button, hover_color):
        """Button hover enter effect"""
        button.config(bg=hover_color)
        
    def on_button_leave(self, button, original_color):
        """Button hover leave effect"""
        button.config(bg=original_color)
    
    def on_board_hover_enter(self, button, position):
        """Board button hover enter"""
        if button['state'] == 'normal' and button['text'] == '':
            button.config(bg=self.colors['button_hover'])
    
    def on_board_hover_leave(self, button, position):
        """Board button hover leave"""
        if button['state'] == 'normal' and button['text'] == '':
            button.config(bg=self.colors['bg_tertiary'])
    
    def start_pulse_animation(self):
        """Start subtle pulse animation for accent elements"""
        def pulse():
            # This could be expanded for more complex animations
            self.window.after(2000, pulse)
        pulse()
    
    def select_mode(self, mode):
        """Select game mode with visual feedback"""
        self.game_mode = mode
        
        if mode == 'ai':
            self.difficulty_section.pack(fill='x', padx=15, pady=10)
            self.current_mode_label.config(text="Mode: AI Challenge")
            self.turn_indicator.config(text="You play as X")
        else:
            self.difficulty_section.pack_forget()
            self.current_mode_label.config(text="Mode: Friend Battle")
            self.turn_indicator.config(text="Player 1 is X, Player 2 is O")
        
        self.start_game()
    
    def set_difficulty(self, difficulty):
        """Set AI difficulty with visual updates"""
        self.difficulty = difficulty
        
        # Update difficulty button appearances
        for diff, button in self.difficulty_buttons.items():
            if diff == difficulty:
                colors = {
                    'easy': self.colors['success'],
                    'medium': self.colors['warning'], 
                    'hard': self.colors['danger']
                }
                button.config(bg=colors[diff])
                button.master.config(bg=colors[diff])
            else:
                button.config(bg=self.colors['bg_tertiary'])
                button.master.config(bg=self.colors['bg_tertiary'])
        
        # Update difficulty display
        diff_names = {'easy': 'Beginner', 'medium': 'Intermediate', 'hard': 'Expert'}
        self.current_difficulty_label.config(text=f"Difficulty: {diff_names[difficulty]}")
    
    def start_game(self):
        """Start new game with enhanced visuals"""
        self.game_active = True
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        
        # Enable and reset buttons with improved styling
        for button in self.buttons:
            button.config(
                state='normal',
                text='',
                bg=self.colors['bg_tertiary'],
                fg=self.colors['text_primary'],
                relief='flat',
                bd=0,
                highlightthickness=0
            )
        
        if self.game_mode == 'ai':
            self.status_label.config(text="Your move! Click any cell to start")
        else:
            self.status_label.config(text="Player 1's turn - Make your move!")
    
    def make_move(self, position):
        """Make a move with enhanced visual feedback"""
        if not self.game_active or self.board[position] != ' ':
            return
        
        # Player move
        self.board[position] = self.current_player
        self.update_button(position, self.current_player)
        
        # Check winner
        winner = self.check_winner()
        if winner:
            self.end_game(winner)
            return
        
        if self.is_board_full():
            self.end_game('draw')
            return
        
        if self.game_mode == 'ai' and self.current_player == 'X':
            self.current_player = 'O'
            self.status_label.config(text="AI is calculating optimal move...")
            self.turn_indicator.config(text="AI thinking...")
            
            # AI delay with visual feedback
            delay = {'easy': 500, 'medium': 1000, 'hard': 1500}[self.difficulty]
            self.window.after(delay, self.ai_move)
        else:
            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.game_mode == 'human':
                player_name = "Player 1" if self.current_player == 'X' else "Player 2"
                self.status_label.config(text=f"{player_name}'s turn")
                self.turn_indicator.config(text=f"Current: {self.current_player}")
    
    def ai_move(self):
        """AI makes move with visual enhancements"""
        if not self.game_active:
            return
        
        # Get AI move based on difficulty
        if self.difficulty == 'easy':
            best_move = self.get_random_move()
        elif self.difficulty == 'medium':
            best_move = self.get_best_move() if random.random() < 0.7 else self.get_random_move()
        else:
            best_move = self.get_best_move()
        
        if best_move is not None:
            self.board[best_move] = 'O'
            self.update_button(best_move, 'O')
            
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
                return
            
            if self.is_board_full():
                self.end_game('draw')
                return
            
            self.current_player = 'X'
            self.status_label.config(text="Your turn - Choose your next move")
            self.turn_indicator.config(text="Your move")
    
    def get_random_move(self):
        """Get random move for easy AI"""
        available = self.get_available_moves()
        return random.choice(available) if available else None
    
    def update_button(self, position, player):
        """Update button with enhanced modern styling"""
        if player == 'X':
            color = self.colors['x_gradient_start']
            bg_color = '#2a1810'  # Dark red background
        else:
            color = self.colors['o_gradient_start']
            bg_color = '#1a2e2a'  # Dark teal background
        
        self.buttons[position].config(
            text=player,
            fg=color,
            state='disabled',
            bg=bg_color,
            font=self.fonts['board'],
            relief='flat',
            bd=2,
            highlightbackground=color,
            highlightcolor=color,
            highlightthickness=1
        )
    
    def check_winner(self):
        """Check for winner with enhanced highlighting"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                # Enhanced highlighting for winning combination
                for pos in combo:
                    self.buttons[pos].config(
                        bg=self.colors['win_glow'],
                        fg='#000000',  # Black text for better contrast on gold
                        relief='raised',
                        bd=3,
                        highlightbackground=self.colors['win_glow'],
                        highlightthickness=2
                    )
                return self.board[combo[0]]
        return None
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']
    
    def minimax(self, depth, maximizing_player, alpha=-math.inf, beta=math.inf):
        """Minimax algorithm for AI"""
        winner = self.check_winner_simple()
        
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif self.is_board_full():
            return 0
        
        if maximizing_player:
            max_eval = -math.inf
            for move in self.get_available_moves():
                self.board[move] = 'O'
                eval_score = self.minimax(depth + 1, False, alpha, beta)
                self.board[move] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_available_moves():
                self.board[move] = 'X'
                eval_score = self.minimax(depth + 1, True, alpha, beta)
                self.board[move] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval
    
    def check_winner_simple(self):
        """Simple winner check for AI"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        return None
    
    def get_best_move(self):
        """Get best move using minimax"""
        best_score = -math.inf
        best_move = None
        
        for move in self.get_available_moves():
            self.board[move] = 'O'
            score = self.minimax(0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def end_game(self, result):
        """End game with spectacular visual effects"""
        self.game_active = False
        self.game_count += 1
        
        # Disable all buttons with proper styling
        for button in self.buttons:
            if button['text'] == '':
                button.config(
                    state='disabled', 
                    bg=self.colors['border'],
                    relief='flat',
                    bd=0
                )
        
        # Update scores and show result
        if result == 'draw':
            message = "🤝 Epic Draw!"
            subtitle = "Both players showed great skill!"
            self.status_label.config(text="Draw - Excellent match!")
            self.scores['draw'] += 1
        elif result == 'X':
            if self.game_mode == 'ai':
                message = "🎉 Victory!"
                subtitle = "You defeated the AI! Incredible!"
                self.status_label.config(text="You won! Outstanding performance!")
                self.scores['player'] += 1
            else:
                message = "🏆 Player 1 Wins!"
                subtitle = "Masterful strategy and execution!"
                self.status_label.config(text="Player 1 claims victory!")
                self.scores['player'] += 1
        else:  # O wins
            if self.game_mode == 'ai':
                message = "🤖 AI Victory"
                subtitle = "The machine proves its superiority!"
                self.status_label.config(text="AI wins this round!")
                self.scores['opponent'] += 1
            else:
                message = "🏆 Player 2 Wins!"
                subtitle = "Strategic brilliance on display!"
                self.status_label.config(text="Player 2 takes the crown!")
                self.scores['opponent'] += 1
        
        self.update_statistics_display()
        self.show_ultra_modern_result_dialog(message, subtitle)
    
    def show_ultra_modern_result_dialog(self, title, subtitle):
        """Show ultra-modern result dialog with enhanced styling"""
        result_window = tk.Toplevel(self.window)
        result_window.title("Game Result")
        result_window.geometry("600x400")
        result_window.configure(bg=self.colors['bg_primary'])
        result_window.resizable(False, False)
        
        # Make it modal and always on top
        result_window.transient(self.window)
        result_window.grab_set()
        result_window.attributes('-topmost', True)
        
        # Center on parent window
        x = self.window.winfo_x() + (self.window.winfo_width() // 2) - 300
        y = self.window.winfo_y() + (self.window.winfo_height() // 2) - 200
        result_window.geometry(f"600x400+{x}+{y}")
        
        # Main container with padding
        main_container = tk.Frame(result_window, bg=self.colors['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header section with enhanced styling
        header_frame = tk.Frame(main_container, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Title with icon and styling
        title_container = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        title_container.pack(fill='x', pady=20)
        
        title_label = tk.Label(
            title_container,
            text=title,
            font=('Segoe UI', 28, 'bold'),
            fg=self.colors['accent_primary'],
            bg=self.colors['bg_secondary']
        )
        title_label.pack()
        
        # Decorative line
        line_frame = tk.Frame(header_frame, bg=self.colors['accent_primary'], height=3)
        line_frame.pack(fill='x', padx=50, pady=(10, 0))
        
        # Content section
        content_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        content_frame.pack(fill='both', expand=True, pady=10)
        
        # Subtitle with better spacing
        subtitle_label = tk.Label(
            content_frame,
            text=subtitle,
            font=('Segoe UI', 14, 'normal'),
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_primary'],
            wraplength=500,
            justify='center'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Stats section with enhanced layout
        stats_container = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='flat')
        stats_container.pack(fill='x', pady=(0, 30), padx=20)
        
        stats_title = tk.Label(
            stats_container,
            text="📊 Session Statistics",
            font=('Segoe UI', 16, 'bold'),
            fg=self.colors['text_primary'],
            bg=self.colors['bg_secondary']
        )
        stats_title.pack(pady=(15, 10))
        
        # Stats grid
        stats_grid = tk.Frame(stats_container, bg=self.colors['bg_secondary'])
        stats_grid.pack(pady=(0, 15))
        
        # Individual stat items
        stat_items = [
            ("🎮", "Games Played", str(self.game_count)),
            ("🏆", "Wins", str(self.scores['player'])),
            ("💀", "Losses", str(self.scores['opponent'])),
            ("🤝", "Draws", str(self.scores['draw']))
        ]
        
        for i, (icon, label, value) in enumerate(stat_items):
            stat_frame = tk.Frame(stats_grid, bg=self.colors['bg_tertiary'], relief='flat')
            stat_frame.grid(row=0, column=i, padx=10, pady=5, sticky='ew')
            
            # Configure column weights
            stats_grid.grid_columnconfigure(i, weight=1)
            
            icon_label = tk.Label(
                stat_frame,
                text=icon,
                font=('Segoe UI', 18),
                fg=self.colors['accent_primary'],
                bg=self.colors['bg_tertiary']
            )
            icon_label.pack(pady=(10, 5))
            
            value_label = tk.Label(
                stat_frame,
                text=value,
                font=('Segoe UI', 20, 'bold'),
                fg=self.colors['text_primary'],
                bg=self.colors['bg_tertiary']
            )
            value_label.pack()
            
            label_label = tk.Label(
                stat_frame,
                text=label,
                font=('Segoe UI', 10),
                fg=self.colors['text_secondary'],
                bg=self.colors['bg_tertiary']
            )
            label_label.pack(pady=(0, 10))
        
        # Win rate display
        if self.game_count > 0:
            win_rate = (self.scores['player'] / self.game_count) * 100
            win_rate_text = f"📈 Win Rate: {win_rate:.1f}%"
        else:
            win_rate_text = "📈 Win Rate: N/A"
        
        win_rate_label = tk.Label(
            stats_container,
            text=win_rate_text,
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['success'] if win_rate > 50 else self.colors['warning'] if win_rate > 25 else self.colors['danger'],
            bg=self.colors['bg_secondary']
        )
        win_rate_label.pack(pady=(0, 15))
        
        # Buttons section
        button_container = tk.Frame(main_container, bg=self.colors['bg_primary'])
        button_container.pack(fill='x', pady=(20, 0))
        
        # Center the buttons
        button_frame = tk.Frame(button_container, bg=self.colors['bg_primary'])
        button_frame.pack()
        
        # Play again button with enhanced styling
        play_again_btn = tk.Button(
            button_frame,
            text="🔄 PLAY AGAIN",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['text_primary'],
            padx=30, pady=15,
            command=lambda: [result_window.destroy(), self.reset_game()],
            cursor='hand2',
            relief='flat',
            bd=0,
            activebackground='#00a085',
            activeforeground=self.colors['text_primary']
        )
        play_again_btn.pack(side='left', padx=15)
        
        # Continue button
        continue_btn = tk.Button(
            button_frame,
            text="✓ CONTINUE",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['accent_primary'],
            fg=self.colors['text_primary'],
            padx=30, pady=15,
            command=result_window.destroy,
            cursor='hand2',
            relief='flat',
            bd=0,
            activebackground=self.colors['accent_secondary'],
            activeforeground=self.colors['text_primary']
        )
        continue_btn.pack(side='left', padx=15)
        
        # Close button
        close_btn = tk.Button(
            button_frame,
            text="❌ CLOSE",
            font=('Segoe UI', 12, 'bold'),
            bg=self.colors['danger'],
            fg=self.colors['text_primary'],
            padx=25, pady=12,
            command=lambda: [result_window.destroy(), self.window.quit()],
            cursor='hand2',
            relief='flat',
            bd=0,
            activebackground='#d63384',
            activeforeground=self.colors['text_primary']
        )
        close_btn.pack(side='left', padx=15)
        
        # Add hover effects for buttons
        def on_button_hover(button, enter_color, leave_color):
            def on_enter(e):
                button.config(bg=enter_color)
            def on_leave(e):
                button.config(bg=leave_color)
            return on_enter, on_leave
        
        play_enter, play_leave = on_button_hover(play_again_btn, '#00a085', self.colors['success'])
        play_again_btn.bind("<Enter>", play_enter)
        play_again_btn.bind("<Leave>", play_leave)
        
        cont_enter, cont_leave = on_button_hover(continue_btn, self.colors['accent_secondary'], self.colors['accent_primary'])
        continue_btn.bind("<Enter>", cont_enter)
        continue_btn.bind("<Leave>", cont_leave)
        
        close_enter, close_leave = on_button_hover(close_btn, '#d63384', self.colors['danger'])
        close_btn.bind("<Enter>", close_enter)
        close_btn.bind("<Leave>", close_leave)
        
        # Focus on continue button by default
        continue_btn.focus_set()
        
        # Keyboard shortcuts
        result_window.bind('<Return>', lambda e: continue_btn.invoke())
        result_window.bind('<Escape>', lambda e: result_window.destroy())
        result_window.bind('<space>', lambda e: play_again_btn.invoke())
    
    def update_statistics_display(self):
        """Update all statistics displays"""
        # Update individual stat labels
        self.wins_label.config(text=f"🏆 Wins: {self.scores['player']}")
        self.losses_label.config(text=f"💀 Losses: {self.scores['opponent']}")
        self.draws_label.config(text=f"🤝 Draws: {self.scores['draw']}")
        self.games_played_label.config(text=f"Games Played: {self.game_count}")
        
        # Calculate and update win rate
        if self.game_count > 0:
            win_rate = (self.scores['player'] / self.game_count) * 100
            self.winrate_label.config(text=f"📈 Win Rate: {win_rate:.1f}%")
        else:
            self.winrate_label.config(text="📈 Win Rate: 0%")
    
    def reset_game(self):
        """Reset game with enhanced visual feedback"""
        self.game_active = False
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        
        # Reset buttons with improved styling
        for button in self.buttons:
            button.config(
                text='',
                state='disabled',
                bg=self.colors['bg_tertiary'],
                fg=self.colors['text_primary'],
                relief='flat',
                bd=0,
                highlightthickness=0
            )
        
        self.status_label.config(text="Select a game mode to begin your journey")
        self.turn_indicator.config(text="")
    
    def reset_scores(self):
        """Reset all scores with confirmation"""
        self.scores = {'player': 0, 'opponent': 0, 'draw': 0}
        self.game_count = 0
        self.update_statistics_display()
        
        # Show ultra-modern confirmation
        confirm_window = tk.Toplevel(self.window)
        confirm_window.title("Statistics Reset")
        confirm_window.geometry("400x200")
        confirm_window.configure(bg=self.colors['bg_secondary'])
        confirm_window.resizable(False, False)
        confirm_window.transient(self.window)
        confirm_window.grab_set()
        
        # Center on parent
        x = self.window.winfo_x() + (self.window.winfo_width() // 2) - 200
        y = self.window.winfo_y() + (self.window.winfo_height() // 2) - 100
        confirm_window.geometry(f"400x200+{x}+{y}")
        
        tk.Label(
            confirm_window,
            text="📊 Statistics Reset Complete!",
            font=self.fonts['heading'],
            fg=self.colors['text_primary'],
            bg=self.colors['bg_secondary']
        ).pack(pady=40)
        
        tk.Label(
            confirm_window,
            text="All game statistics have been cleared.",
            font=self.fonts['body'],
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_secondary']
        ).pack(pady=(0, 20))
        
        tk.Button(
            confirm_window,
            text="✓ UNDERSTOOD",
            font=self.fonts['button'],
            bg=self.colors['success'],
            fg=self.colors['text_primary'],
            padx=25, pady=10,
            command=confirm_window.destroy,
            cursor='hand2',
            relief='flat',
            bd=0
        ).pack()
    
    def run(self):
        """Run the ultra-modern game"""
        self.window.mainloop()

def main():
    game = UltraModernTicTacToe()
    game.run()

if __name__ == "__main__":
    main()
