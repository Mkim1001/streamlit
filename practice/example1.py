import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Function to generate 3D star coordinates
def generate_star_coordinates(n_stars):
    x_coords = np.random.rand(n_stars) * 100
    y_coords = np.random.rand(n_stars) * 100
    z_coords = np.random.rand(n_stars) * 100
    return x_coords, y_coords, z_coords

def app():
    # Inject CSS for setting the Streamlit app background image
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover;
            background-position: center;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Interactive 3D Star Coordinates Generator")

    n_stars = st.number_input("Enter the number of stars to generate in 3D space:", min_value=1, value=50)

    if st.button("Generate Stars in 3D"):
        x_coords, y_coords, z_coords = generate_star_coordinates(n_stars)

        fig = go.Figure(data=[go.Scatter3d(
            x=x_coords,
            y=y_coords,
            z=z_coords,
            mode='markers',
            marker=dict(size=5, color='yellow', opacity=0.8)
        )])

        # Adjusting the size of the figure. Assuming the original size to be doubled
        fig_width = 800  # Example original width
        fig_height = 600  # Example original height
        fig.update_layout(width=fig_width * 2, height=fig_height * 2,
                          margin=dict(l=0, r=0, b=0, t=0),
                          paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor='rgba(0,0,0,0)',
                          scene=dict(
                              xaxis=dict(showbackground=False),
                              yaxis=dict(showbackground=False),
                              zaxis=dict(showbackground=False),
                          ))

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    app()
