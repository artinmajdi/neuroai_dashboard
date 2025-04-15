import streamlit as st
import os
from streamlit_elements import elements, mui, html

def render_grant_slides(grant_type):
    """
    Renders grant slides using streamlit-elements with Material UI components

    Args:
        grant_type (str): Type of grant to render ("NIH K99/R00", "NSF CAREER", or "McKnight Scholars")
    """
    # Map grant types to their corresponding styles and titles
    grant_styles = {
        "NIH K99/R00": {
            "gradient": "linear-gradient(to right, #1a5276, #2980b9)",
            "color": "#2980b9",
            "title": "NIH BRAIN Initiative K99/R00",
            "subtitle": "Pathway to Independence Award",
            "tagline": "A Funding Strategy for NeuroAI Research"
        },
        "NSF CAREER": {
            "gradient": "linear-gradient(to right, #145a32, #27ae60)",
            "color": "#27ae60",
            "title": "NSF CAREER Award",
            "subtitle": "Advancing NeuroAI through Integrated Research and Education",
            "tagline": "A Five-Year Research and Education Plan"
        },
        "McKnight Scholars": {
            "gradient": "linear-gradient(to right, #4a235a, #8e44ad)",
            "color": "#8e44ad",
            "title": "McKnight Scholars Award",
            "subtitle": "Explainable NeuroAI for Neural Circuit Understanding",
            "tagline": "A Three-Year Research Proposal"
        }
    }

    style = grant_styles.get(grant_type, grant_styles["NIH K99/R00"])

    # Use streamlit-elements to create a Material UI based presentation
    with elements("grant_slides"):
        # Create a container with styling
        with mui.Box(
            sx={
                "width": "100%",
                "maxWidth": "900px",
                "margin": "0 auto",
                "fontFamily": "'Roboto', 'Helvetica', 'Arial', sans-serif",
            }
        ):
            # Title slide
            with mui.Paper(
                elevation=3,
                sx={
                    "background": style["gradient"],
                    "color": "white",
                    "padding": "2rem",
                    "borderRadius": "10px",
                    "marginBottom": "2rem",
                    "textAlign": "center"
                }
            ):
                mui.Typography(style["title"], variant="h4", component="h1", gutterBottom=True)
                mui.Typography(style["subtitle"], variant="h5", component="h2", gutterBottom=True)
                mui.Typography(style["tagline"], variant="subtitle1", component="p", sx={"fontStyle": "italic"})
                mui.Typography(
                    "Prepared for: Mass General Brigham NeuroAI Center Interview",
                    variant="caption",
                    component="div",
                    sx={"marginTop": "1.5rem", "opacity": "0.8"}
                )

            # Overview slide
            render_slide(
                "Overview & Purpose",
                style["color"],
                [
                    {
                        "title": "Program Description",
                        "bullets": [
                            f"Key funding mechanism for {grant_type}",
                            "Supports innovative research in NeuroAI",
                            "Emphasis on translational applications",
                            "Competitive selection process"
                        ]
                    },
                    {
                        "title": "Key Benefits",
                        "bullets": [
                            "Substantial funding for research program",
                            "Career advancement and recognition",
                            "Access to specialized resources and networks",
                            "Platform for future funding opportunities"
                        ]
                    }
                ]
            )

            # Eligibility slide
            render_slide(
                "Eligibility & Requirements",
                style["color"],
                [
                    {
                        "title": "Eligibility Criteria",
                        "bullets": [
                            "Early-career researchers and scientists",
                            "Strong publication record in relevant fields",
                            "Innovative research proposal with clear objectives",
                            "Institutional support and resources"
                        ]
                    },
                    {
                        "title": "Application Components",
                        "bullets": [
                            "Detailed research plan with timeline",
                            "Preliminary data supporting feasibility",
                            "Budget justification and resource allocation",
                            "Letters of support and collaboration"
                        ]
                    }
                ]
            )

            # Alignment slide
            render_slide(
                "Alignment with NeuroAI Center",
                style["color"],
                [
                    {
                        "title": "Strategic Alignment",
                        "bullets": [
                            "Multimodal data integration approaches",
                            "Explainable AI methods for clinical interpretation",
                            "Focus on neurological recovery mechanisms",
                            "Translational research with clinical applications"
                        ],
                        "fullWidth": True
                    }
                ]
            )

            # Timeline slide
            render_slide(
                "Timeline & Strategy",
                style["color"],
                [
                    {
                        "title": "Key Dates",
                        "bullets": [
                            "Proposal development: 3-6 months",
                            "Submission deadlines vary by program",
                            "Review process: typically 6-9 months",
                            "Project start: within 3-6 months of award"
                        ]
                    },
                    {
                        "title": "Application Strategy",
                        "bullets": [
                            "Leverage center's unique datasets and resources",
                            "Incorporate mentorship from center leadership",
                            "Include preliminary results from initial projects",
                            "Highlight interdisciplinary collaboration potential"
                        ]
                    }
                ]
            )

            # Outcomes slide
            render_slide(
                "Expected Outcomes",
                style["color"],
                [
                    {
                        "title": "Research Deliverables",
                        "bullets": [
                            "Novel computational methods and algorithms",
                            "Validation in clinical datasets",
                            "Open-source software and tools",
                            "High-impact publications"
                        ]
                    },
                    {
                        "title": "Career Advancement",
                        "bullets": [
                            "Establish independent research program",
                            "Build collaborative network",
                            "Develop clinical partnerships",
                            "Foundation for future grant applications"
                        ]
                    }
                ]
            )

def render_slide(title, color, sections):
    """Helper function to render a slide with Material UI components"""
    with mui.Paper(elevation=2, sx={"marginBottom": "2rem", "overflow": "hidden"}):
        # Slide title
        mui.Box(
            sx={
                "background": f"linear-gradient(to right, {color}, {color}90)",
                "color": "white",
                "padding": "1rem",
                "borderTopLeftRadius": "4px",
                "borderTopRightRadius": "4px"
            },
            children=[
                mui.Typography(title, variant="h6", component="h2")
            ]
        )

        # Slide content
        with mui.Box(sx={"padding": "1.5rem", "backgroundColor": "white"}):
            # Create grid layout based on number of sections
            grid_template = "1fr" if any(section.get("fullWidth", False) for section in sections) else " ".join(["1fr"] * len(sections))

            with mui.Box(
                sx={
                    "display": "grid",
                    "gridTemplateColumns": grid_template,
                    "gap": "1.5rem"
                }
            ):
                # Render each section
                for section in sections:
                    with mui.Box():
                        mui.Typography(
                            section["title"],
                            variant="subtitle1",
                            component="h3",
                            sx={
                                "color": color,
                                "fontWeight": "bold",
                                "marginBottom": "0.75rem"
                            }
                        )

                        # Render bullet points
                        for bullet in section["bullets"]:
                            with mui.Box(sx={"display": "flex", "alignItems": "flex-start", "marginBottom": "0.5rem"}):
                                mui.Typography(
                                    "•",
                                    sx={
                                        "color": color,
                                        "fontWeight": "bold",
                                        "marginRight": "0.5rem",
                                        "marginTop": "0.1rem"
                                    }
                                )
                                mui.Typography(bullet)
