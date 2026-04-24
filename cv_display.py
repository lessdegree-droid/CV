import tkinter as tk
from tkinter import font as tkFont
import webbrowser

class CVApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("MUJAHID HAYATKHAN - CV")
        self.root.geometry("1000x1200")
        self.root.configure(bg="#f5f5f5")
        
        # CV Data
        self.cv_data = {
            "name": "MUJAHID HAYATKHAN",
            "email": "mujahidahayatkhan@gmail.com",
            "phone": "+91-9108327198",
            "location": "Belagavi, Karnataka, India",
            "portfolio": "in/mujahid-h1/utmportfolio",
            "website": "behance.net/mujahidhayatkh",
            "summary": "Computational designer specializing in BIM workflows, parametric modeling, and digital visualization. Skilled in developing and managing Revit models, preparing technical drawings, and coordinating multidisciplinary teams. Proficient in Rhino, Grasshopper, Dynamo, Python, and C# scripting, applying computational methods to automate workflows and optimize design solutions.",
            "experience": [
                {
                    "title": "Junior Architect",
                    "company": "Simpliforge 3D-Creation",
                    "period": "November 2025 - February 2026",
                    "location": "Hyderabad, Telangana, India",
                    "details": [
                        "Façade and computational design support using parametric workflows with Grasshopper, Rhino, Rhino Python, and C# scripting",
                        "Involved in robotic concrete 3D printing, digital fabrication, and technical documentation using Robot Studio and AutoCAD",
                        "Developed digital fabrication prototypes by integrating advanced scripting and simulation tools",
                        "Devised parametric scripts to streamline architectural geometry generation"
                    ]
                },
                {
                    "title": "Intern Architect",
                    "company": "Saleem Toad Architects",
                    "period": "January 2024 - April 2024",
                    "location": "Belgaum, Karnataka, India",
                    "details": [
                        "Completed an academic internship focused on design development and interior detailing",
                        "Drafted construction documents and architectural details for residential and commercial projects",
                        "Engineered 8+ schematic design sets per semester using Autodesk Revit",
                        "Directed weekly BIM model coordination sessions with project teams"
                    ]
                },
                {
                    "title": "Assistant Engineer",
                    "company": "Hayatkhan Construction",
                    "period": "June 2019 - August 2020",
                    "location": "Kudachi, Karnataka, India",
                    "details": [
                        "Developed and managed BIM models in Revit, integrating parametric workflows",
                        "Prepared blueprint drawings and digital documentation ensuring compliance with design standards",
                        "Conducted site visits to monitor progress and identify issues",
                        "Coordinated with multidisciplinary teams to align architectural, structural, and MEP systems"
                    ]
                }
            ],
            "education": [
                {
                    "degree": "Bachelor of Architecture",
                    "school": "Gopte Institute Of Technology",
                    "location": "Belgaum, Karnataka, India",
                    "year": "2025",
                    "details": "Five-year undergraduate degree in architecture with emphasis on design, construction, and professional practice"
                },
                {
                    "degree": "Diploma in Civil Engineering",
                    "school": "Department Of Technical Education Karnataka",
                    "location": "Belgaum, Karnataka, India",
                    "year": "2019",
                    "details": "Three-year program covering structural design, construction techniques, and material science"
                }
            ],
            "skills": {
                "Design & Modeling": ["Revit", "AutoCAD", "Rhino 3D", "SketchUp", "Blender", "3ds Max", "ArchiCAD", "Navisworks"],
                "Programming & Scripting": ["Python", "C#", "Rhino Python", "Dynamo", "VS Code", "GitHub"],
                "Rendering & Visualization": ["Lumion", "Enscape", "D5 Render", "V-Ray", "Adobe Photoshop", "InDesign"],
                "Technical Tools": ["Grasshopper", "STAAD Pro", "Robot Studio", "Robot Studio", "MS Office", "Comfy UI"],
                "Other": ["BIM Workflows", "Digital Fabrication", "Parametric Modeling", "Clash Detection", "ArcGIS", "English", "Arabic"]
            }
        }
        
        self.create_gui()
    
    def create_gui(self):
        # Create main scrollable frame
        main_canvas = tk.Canvas(self.root, bg="#f5f5f5", highlightthickness=0)
        main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=main_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        content_frame = tk.Frame(main_canvas, bg="#f5f5f5")
        main_canvas.create_window((0, 0), window=content_frame, anchor=tk.NW, width=950)
        
        # Header with name and contact
        self.add_header(content_frame)
        
        # Professional Summary
        self.add_section(content_frame, "PROFESSIONAL SUMMARY")
        summary_font = tkFont.Font(family="Segoe UI", size=10)
        summary_label = tk.Label(content_frame, text=self.cv_data["summary"], 
                                font=summary_font, bg="#f5f5f5", fg="#333333", 
                                wraplength=900, justify=tk.LEFT)
        summary_label.pack(anchor=tk.NW, padx=30, pady=(0, 20), fill=tk.X)
        
        # Experience Section
        self.add_section(content_frame, "EXPERIENCE")
        for exp in self.cv_data["experience"]:
            self.add_experience(content_frame, exp)
        
        # Education Section
        self.add_section(content_frame, "EDUCATION")
        for edu in self.cv_data["education"]:
            self.add_education(content_frame, edu)
        
        # Skills Section
        self.add_section(content_frame, "SKILLS")
        self.add_skills(content_frame, self.cv_data["skills"])
        
        # Footer spacing
        tk.Frame(content_frame, bg="#f5f5f5", height=30).pack()
        
        content_frame.update_idletasks()
        main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        
        # Bind mouse wheel to scroll
        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def add_header(self, parent):
        # Header background
        header_bg = tk.Frame(parent, bg="#1e3a5f", height=150)
        header_bg.pack(fill=tk.X, pady=(0, 20))
        
        # Name
        name_font = tkFont.Font(family="Segoe UI", size=32, weight="bold")
        name_label = tk.Label(header_bg, text=self.cv_data["name"], 
                             font=name_font, bg="#1e3a5f", fg="#ffffff")
        name_label.pack(anchor=tk.W, padx=30, pady=(15, 5))
        
        # Contact info
        contact_font = tkFont.Font(family="Segoe UI", size=9)
        contact_text = f"📧 {self.cv_data['email']}  |  📱 {self.cv_data['phone']}"
        contact_label = tk.Label(header_bg, text=contact_text, 
                                font=contact_font, bg="#1e3a5f", fg="#e0e0e0")
        contact_label.pack(anchor=tk.W, padx=30, pady=2)
        
        location_text = f"📍 {self.cv_data['location']}"
        location_label = tk.Label(header_bg, text=location_text, 
                                 font=contact_font, bg="#1e3a5f", fg="#e0e0e0")
        location_label.pack(anchor=tk.W, padx=30, pady=2)
        
        portfolio_text = f"🌐 {self.cv_data['website']}"
        portfolio_label = tk.Label(header_bg, text=portfolio_text, 
                                  font=contact_font, bg="#1e3a5f", fg="#e0e0e0")
        portfolio_label.pack(anchor=tk.W, padx=30, pady=(2, 15))
    
    def add_section(self, parent, title):
        title_font = tkFont.Font(family="Segoe UI", size=14, weight="bold")
        title_label = tk.Label(parent, text=title, font=title_font, bg="#f5f5f5", fg="#1e3a5f")
        title_label.pack(anchor=tk.W, padx=30, pady=(20, 5))
        
        # Underline
        line = tk.Frame(parent, bg="#2196F3", height=2)
        line.pack(anchor=tk.W, padx=30, fill=tk.X, pady=(0, 15))
    
    def add_experience(self, parent, exp):
        exp_frame = tk.Frame(parent, bg="#ffffff", relief=tk.FLAT, bd=0)
        exp_frame.pack(anchor=tk.NW, padx=30, pady=(0, 15), fill=tk.X)
        
        # Title
        title_font = tkFont.Font(family="Segoe UI", size=11, weight="bold")
        title_label = tk.Label(exp_frame, text=exp["title"], font=title_font, 
                              bg="#ffffff", fg="#1e3a5f")
        title_label.pack(anchor=tk.W, padx=15, pady=(10, 0))
        
        # Company and duration
        meta_font = tkFont.Font(family="Segoe UI", size=9)
        meta_text = f"{exp['company']} • {exp['location']}"
        meta_label = tk.Label(exp_frame, text=meta_text, font=meta_font, 
                             bg="#ffffff", fg="#2196F3")
        meta_label.pack(anchor=tk.W, padx=15, pady=2)
        
        period_label = tk.Label(exp_frame, text=exp["period"], font=meta_font, 
                               bg="#ffffff", fg="#888888")
        period_label.pack(anchor=tk.W, padx=15, pady=(0, 8))
        
        # Details
        detail_font = tkFont.Font(family="Segoe UI", size=9)
        for detail in exp["details"]:
            detail_label = tk.Label(exp_frame, text=f"• {detail}", font=detail_font, 
                                   bg="#ffffff", fg="#555555", wraplength=850, justify=tk.LEFT)
            detail_label.pack(anchor=tk.NW, padx=25, pady=2, fill=tk.X)
        
        tk.Label(exp_frame, text="", bg="#ffffff").pack(pady=5)
    
    def add_education(self, parent, edu):
        edu_frame = tk.Frame(parent, bg="#f9f9f9", relief=tk.FLAT, bd=0)
        edu_frame.pack(anchor=tk.NW, padx=30, pady=(0, 12), fill=tk.X)
        
        # Degree
        degree_font = tkFont.Font(family="Segoe UI", size=11, weight="bold")
        degree_label = tk.Label(edu_frame, text=edu["degree"], font=degree_font, 
                               bg="#f9f9f9", fg="#1e3a5f")
        degree_label.pack(anchor=tk.W, padx=15, pady=(10, 0))
        
        # School and location
        school_font = tkFont.Font(family="Segoe UI", size=9)
        school_text = f"{edu['school']} • {edu['location']}"
        school_label = tk.Label(edu_frame, text=school_text, font=school_font, 
                               bg="#f9f9f9", fg="#2196F3")
        school_label.pack(anchor=tk.W, padx=15, pady=2)
        
        year_label = tk.Label(edu_frame, text=edu["year"], font=school_font, 
                             bg="#f9f9f9", fg="#888888")
        year_label.pack(anchor=tk.W, padx=15, pady=2)
        
        # Details
        details_font = tkFont.Font(family="Segoe UI", size=9)
        details_label = tk.Label(edu_frame, text=edu["details"], font=details_font, 
                                bg="#f9f9f9", fg="#555555", wraplength=850, justify=tk.LEFT)
        details_label.pack(anchor=tk.NW, padx=15, pady=(5, 10), fill=tk.X)
    
    def add_skills(self, parent, skills):
        for category, skill_list in skills.items():
            category_frame = tk.Frame(parent, bg="#f5f5f5")
            category_frame.pack(anchor=tk.W, padx=30, pady=(0, 12), fill=tk.X)
            
            # Category title
            cat_font = tkFont.Font(family="Segoe UI", size=10, weight="bold")
            cat_label = tk.Label(category_frame, text=f"{category}:", font=cat_font, 
                                bg="#f5f5f5", fg="#1e3a5f")
            cat_label.pack(anchor=tk.W, pady=(5, 8))
            
            # Skills as tags
            skills_container = tk.Frame(category_frame, bg="#f5f5f5")
            skills_container.pack(anchor=tk.W, fill=tk.X)
            
            skill_font = tkFont.Font(family="Segoe UI", size=9)
            for skill in skill_list:
                skill_tag = tk.Label(skills_container, text=skill, font=skill_font, 
                                    bg="#e3f2fd", fg="#1976d2", padx=10, pady=4, relief=tk.FLAT)
                skill_tag.pack(side=tk.LEFT, padx=4, pady=3)

def main():
    root = tk.Tk()
    app = CVApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
