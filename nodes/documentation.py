from ..utils.logger import logger

def title(text):
    """Title text element"""
    return f'<div style="margin-bottom: 10px;">{text}</div>'

def short_desc(desc):
    """Create a short description element with the special ID"""
    return f'<div id="Y7_shortdesc" style="margin-bottom: 15px;">{desc}</div>'

def process_highlights(text):
    """Process text and convert `highlighted` parts to code style that works in both light and dark themes"""
    import re
    pattern = r'`([^`]+)`'
    # Theme-agnostic styling:
    return re.sub(pattern, r'<code style="border: 1px solid #666; border-radius: 3px; padding: 0px 1px; font-family: monospace; display: inline-block;">\1</code>', text)
    
# Then modify normal to use this
def normal(text, indent_level=0, font_size="12px"):
    """Normal text element with optional indentation and font size"""
    indent_px = indent_level * 20  # 20px per indent level
    processed_text = process_highlights(text)
    return f'<div style="margin-bottom: 8px; margin-left: {indent_px}px; font-size: {font_size};">{processed_text}</div>'

descriptions = {

    "Y7_SideBySide": [
        "2D To 3D Image Converter",
        short_desc("Converts a 2D image to stereoscopic 3D image"),
        normal("Processes an image and its depth map to generate an SBS (side-by-side) stereoscopic 3D image."),
        normal("Inputs:"),
        normal("- `base_image`: The main image to convert to a side-by-side 3D image.", 1),
        normal("- `depth_map`: Grayscale depth map of the base image.", 1),        
        normal("- method: `mesh_warping` or `grid_sampling` to shift pixels based on the depth map.", 1),        
        normal("- `depth_scale`: Controls the strength of the 3D effect (default: 40). Higher values create more pronounced depth but at the cost of tearing and artefacts.", 1),
        normal("- `mode`: Viewing mode:", 1),
        normal("  - parallel: For parallel viewing (left eye sees left image, right sees right image).", 2),
        normal("  - cross_eyed: For cross-eyed viewing (left eye sees right image and vice versa).", 2),
        normal("  - For more info about parallel vs cross-eyed <a href='https://www.ks.uiuc.edu/Research/vmd/vmd-1.7.1/ug/node97.html#:~:text=In%20cross%2Deyed%20stereo%2C%20the,hence%20the%20name%20cross%2Deyed.' target='_blank'>visit here.</a>", 2),
        normal("- `depth_blur_strength`: Controls how much to blur the depth map transitions (3-33, odd values only)", 1),
        normal("   - Lower values for sharper depth separation between objects or layers.", 2),
        normal("   - Higher values for smoother transitions between depth planes, though this may introduce some distortion in some images.", 2),
        normal("Output:"),
        normal("- A side-by-side stereoscopic image with twice the width of the original image.", 1),
            
    ],

    "Y7_VideoSideBySide": [
        "2D To 3D Video Converter",
        short_desc("Converts a 2D video to a stereoscopic 3D video from its frames and depth maps"),
        normal("Processes a sequence of video frames to create an SBS (side-by-side) stereoscopic 3D video."),
        normal("Inputs:"),
        normal("- `frames`: Sequence of video frames to convert to side-by-side 3D.", 1),
        normal("- `depth_maps`: Sequence of depth maps corresponding to each frame.", 1),
        normal("- method: `mesh_warping` or `grid_sampling` to shift pixels based on the depth map.", 1),        
        normal("- `depth_scale`: Controls the strength of the 3D effect (default: 40). Higher values create more pronounced depth but at the cost of tearing and artefacts.", 1),
        normal("- `mode`: Viewing mode:", 1),
        normal("  - parallel: For parallel viewing (left eye sees left image).", 2),
        normal("  - cross_eyed: For cross-eyed viewing (left eye sees right image ande vice versa).", 2),
        normal("  - For more info about parallel vs cross-eyed <a href='https://www.ks.uiuc.edu/Research/vmd/vmd-1.7.1/ug/node97.html#:~:text=In%20cross%2Deyed%20stereo%2C%20the,hence%20the%20name%20cross%2Deyed.' target='_blank'>visit here.</a>", 2),
        normal("- `depth_blur_strength`: Controls how much to blur the depth map transitions (3-33, odd values only)", 1),
        normal("   - Lower values for sharper depth separation between objects or layers.", 2),
        normal("   - Higher values for smoother transitions between depth planes, though this may introduce some distortion in some images.", 2),
        normal("- `temporal_smoothing`: Controls smoothing between frames (0.0-0.5). Higher values create more consistent depth perception between frames but may reduce responsiveness to rapid depth changes.", 1),
        normal("-  `batch-size`: Number of frames to process at once. Lower values = less memory, but maybe slower."),
        normal("Output:"),
        normal("- A sequence of side-by-side stereoscopic frames.", 1),
        normal("Usage (see example workflow):"),
        normal("1. Use one of the 'Load Video' nodes from Video Helper Suite to extract frames", 1),
        normal("2. Use 'DepthAnythingV2' nodes to generate depth maps for each frame", 1),
        normal("3. Feed both into this node to create SBS 3D frames", 1),
        normal("4. Use the 'Video Combine' node from the video helper suite to rebuild the video", 1),
    ],

    "Y7_LenticularDisplay": [
        "Multi-View 3D for Lenticular Displays",
        short_desc("Generates multiple viewing angles for naked eye 3D lenticular displays"),
        normal("Processes an image and its depth map to generate multiple views arranged in a grid, suitable for lenticular displays (naked eye 3D)."),
        normal("Inputs:"),
        normal("- `base_image`: The main image to convert to multi-view format.", 1),
        normal("- `depth_map`: Grayscale depth map of the base image.", 1),
        normal("- `method`: `mesh_warping` or `grid_sampling` to shift pixels based on the depth map.", 1),
        normal("- `num_views`: Number of viewing angles to generate (default: 40 for typical lenticular displays).", 1),
        normal("- `depth_scale`: Controls the strength of the 3D effect (default: 5). Lower values (3-10) work well for lenticular displays.", 1),
        normal("- `convergence`: Sets the depth plane (0.0-1.0):", 1),
        normal("  - 0.0: Objects appear to protrude from the screen (pop-out effect).", 2),
        normal("  - 0.5: Balanced depth with some objects protruding and some receding.", 2),
        normal("  - 1.0: Objects appear to recede into the screen (depth effect).", 2),
        normal("- `grid_layout`: Output arrangement pattern:", 1),
        normal("  - z_pattern: Left-to-right, top-to-bottom (standard).", 2),
        normal("  - column_first: Top-to-bottom, left-to-right.", 2),
        normal("- `grid_columns`: Number of columns in the output grid (default: 8).", 1),
        normal("- `depth_blur_strength`: Controls how much to blur the depth map transitions (3-33, odd values only).", 1),
        normal("Output:"),
        normal("- A grid image containing all generated views arranged according to the specified layout.", 1),
        normal("Use Case:"),
        normal("- Designed for lenticular displays that show different images based on viewing angle.", 1),
        normal("- Views are centered around the original image position and distributed evenly left and right.", 1),
    ],

    "Y7_VideoLenticularDisplay": [
        "Multi-View 3D Video for Lenticular Displays",
        short_desc("Generates multiple viewing angles for video sequences on naked eye 3D lenticular displays"),
        normal("Processes video frames and their depth maps to generate multiple views per frame arranged in a grid, suitable for lenticular displays."),
        normal("Inputs:"),
        normal("- `frames`: Sequence of video frames to convert to multi-view format.", 1),
        normal("- `depth_maps`: Sequence of depth maps corresponding to each frame.", 1),
        normal("- `method`: `mesh_warping` or `grid_sampling` to shift pixels based on the depth map.", 1),
        normal("- `num_views`: Number of viewing angles to generate per frame (default: 40).", 1),
        normal("- `depth_scale`: Controls the strength of the 3D effect (default: 5). Lower values work well for lenticular displays.", 1),
        normal("- `convergence`: Sets the depth plane (0.0-1.0, default: 0.5).", 1),
        normal("- `grid_layout`: Output arrangement pattern (z_pattern or column_first).", 1),
        normal("- `grid_columns`: Number of columns in the output grid (default: 8).", 1),
        normal("- `depth_blur_strength`: Controls how much to blur the depth map transitions (3-33, odd values only).", 1),
        normal("- `temporal_smoothing`: Controls smoothing between frames (0.0-0.5). Higher values create more consistent depth perception.", 1),
        normal("- `batch_size`: Number of frames to process at once. Lower values use less memory.", 1),
        normal("Output:"),
        normal("- A sequence of grid images, each containing all views for that frame.", 1),
        normal("Use Case:"),
        normal("- Designed for creating video content for lenticular displays.", 1),
        normal("- Similar to Y7_LenticularDisplay but processes video sequences with temporal smoothing.", 1),
    ],

    # Add more node descriptions here
}

def as_html(entry, depth=0):
    """Convert structured documentation into HTML with collapsible sections"""
    if isinstance(entry, dict):
        size = 0.8 if depth < 2 else 1
        html = ''
        for k in entry:
            if k == "collapsed":
                continue
            collapse_single = k.endswith("_collapsed")
            if collapse_single:
                name = k[:-len("_collapsed")]
            else:
                name = k
            if collapse_single:
                name = k[:-len("_collapsed")]
            else:
                name = k
            collapse_flag = ' Y7_SBS_precollapse' if entry.get("collapsed", False) or collapse_single else ''
            html += f'<div Y7_SBS_title=\"{name}\" style=\"display: flex; font-size: {size}em\" class=\"Y7_SBS_collapse{collapse_flag}\"><div style=\"color: #AAA; height: 1.5em;\">[<span style=\"font-family: monospace\">-</span>]</div><div style=\"width: 100%\">{name}: {as_html(entry[k], depth=depth+1)}</div></div>'
        return html
    if isinstance(entry, list):
        if depth == 0:
            depth += 1
            size = .8
        else:
            size = 1
        html = ''
        html += entry[0]
        for i in entry[1:]:
            html += f'<div style=\"font-size: {size}em\">{as_html(i, depth=depth)}</div>'
        return html
    return str(entry)

def format_descriptions(nodes):
    """Applies HTML documentation to node classes"""
    logger.info(f"Formatting descriptions for nodes: {list(nodes.keys())}")
    logger.info(f"Available descriptions: {list(descriptions.keys())}")
    
    for k in descriptions:
        if k in nodes:
            logger.info(f"Setting DESCRIPTION for {k}")
            nodes[k].DESCRIPTION = as_html(descriptions[k])
            # Also set a direct description property for easier access
            nodes[k].description = as_html(descriptions[k])
        else:
            logger.warning(f"Node {k} has a description but is not in the nodes dictionary")
    
    # Optionally, log any undocumented nodes
    undocumented_nodes = []
    for k in nodes:
        if k.startswith("Y7_") and not hasattr(nodes[k], "DESCRIPTION"):
            undocumented_nodes.append(k)
    
    if len(undocumented_nodes) > 0:
        logger.warning(f"Some nodes have not been documented: {undocumented_nodes}")
    
    # Return the number of descriptions applied for confirmation
    return len([k for k in descriptions if k in nodes])
