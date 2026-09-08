document.addEventListener("DOMContentLoaded", function () {

    /*
     * ============================================================
     * OPEN PROJECT MODAL
     * ============================================================
     */

    window.openProjectModal = function (projectId) {

        const modal = document.getElementById(
            "project-modal-" + projectId
        );

        if (!modal) {
            console.error(
                "Project modal not found:",
                projectId
            );
            return;
        }

        modal.classList.add("active");

        document.body.classList.add("modal-open");

        // Prevent the page behind the modal from scrolling
        document.body.style.overflow = "hidden";
    };


    /*
     * ============================================================
     * CLOSE PROJECT MODAL
     * ============================================================
     */

    window.closeProjectModal = function (projectId) {

        const modal = document.getElementById(
            "project-modal-" + projectId
        );

        if (!modal) {
            console.error(
                "Project modal not found:",
                projectId
            );
            return;
        }

        modal.classList.remove("active");

        document.body.classList.remove("modal-open");

        // Restore normal page scrolling
        document.body.style.overflow = "";
    };


    /*
     * ============================================================
     * CLOSE WHEN CLICKING MODAL BACKGROUND
     * ============================================================
     */

    window.closeProjectModalOnBackground = function (
        event,
        projectId
    ) {

        /*
         * Only close the modal when the user clicks
         * the dark background itself.
         *
         * Clicking inside the project content will
         * NOT close the modal.
         */

        if (event.target === event.currentTarget) {

            window.closeProjectModal(projectId);

        }
    };


    /*
     * ============================================================
     * CLOSE WITH ESCAPE KEY
     * ============================================================
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

});
