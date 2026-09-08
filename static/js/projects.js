/*
 * ============================================================
 * PROJECT MODAL FUNCTIONS
 * ============================================================
 *
 * These functions are intentionally attached to window because
 * projects.html calls them directly through onclick="..."
 */


/*
 * OPEN PROJECT MODAL
 */
window.openProjectModal = function (projectId) {

    const modal = document.getElementById(
        "project-modal-" + projectId
    );

    if (!modal) {
        console.error(
            "Project modal not found:",
            "project-modal-" + projectId
        );
        return;
    }

    modal.classList.add("active");

    document.body.classList.add("modal-open");

    document.body.style.overflow = "hidden";
};


/*
 * CLOSE PROJECT MODAL
 */
window.closeProjectModal = function (projectId) {

    const modal = document.getElementById(
        "project-modal-" + projectId
    );

    if (!modal) {
        console.error(
            "Project modal not found:",
            "project-modal-" + projectId
        );
        return;
    }

    modal.classList.remove("active");

    document.body.classList.remove("modal-open");

    document.body.style.overflow = "";
};


/*
 * CLOSE WHEN CLICKING THE BACKGROUND
 */
window.closeProjectModalOnBackground = function (
    event,
    projectId
) {

    if (event.target === event.currentTarget) {
        window.closeProjectModal(projectId);
    }
};


/*
 * CLOSE WITH ESCAPE KEY
 */
document.addEventListener("keydown", function (event) {

    if (event.key !== "Escape") {
        return;
    }

    const openModal = document.querySelector(
        ".project-modal.active"
    );

    if (!openModal) {
        return;
    }

    openModal.classList.remove("active");

    document.body.classList.remove("modal-open");

    document.body.style.overflow = "";
});
