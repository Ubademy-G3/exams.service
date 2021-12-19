from infrastructure.db.exam_solution_schema import ExamSolution
import logging

logger = logging.getLogger(__name__)

class ExamSolutionRepositoryPostgres:
    def add_exam_solution(self, db, exam_solution):
        db.add(exam_solution)
        db.commit()

        logger.info("New exam solution added")
        logger.debug("ID of the new exam solution: %s", exam_solution.id)

    def get_exam_solution(self, db, exam_solution_id):
        exam_solution = db.query(ExamSolution).filter(ExamSolution.id == exam_solution_id).first()
        logger.debug("Getting exam solution %s", exam_solution_id)
        return exam_solution

    def get_all_exam_solutions_by_exam_template_id(self, db, exam_template_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.exam_template_id == exam_template_id)
        if graded is not None:
            logger.debug("Get solutions of exam template %s with filter graded %s",
                        exam_template_id, graded)
            query = query.filter(ExamSolution.graded == graded)
        if approval_state is not None:
            logger.debug("Get solutions of exam template %s with filter approval_state %s",
                        exam_template_id, approval_state)
            query = query.filter(ExamSolution.approval_state == approval_state)
        exam_solutions = query.all()
        logger.debug("Getting all solutions of exam template %s", exam_template_id)
        return exam_solutions

    def get_all_exam_solutions_by_user_id(self, db, user_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.user_id == user_id)
        if graded is not None:
            logger.debug("Get solutions of exam for user %s with filter graded %s",
                        user_id, graded)
            query = query.filter(ExamSolution.graded == graded)
        if approval_state is not None:
            logger.debug("Get solutions of exam for user %s with filter approval_state %s",
                        user_id, approval_state)
            query = query.filter(ExamSolution.approval_state == approval_state)
        exam_solutions = query.all()
        logger.debug("Getting all solutions of exam for user %s", user_id)
        return exam_solutions

    def get_all_exam_solutions_by_user_id_and_exam_template_id(self, db, user_id, exam_template_id):
        query = db.query(ExamSolution).filter(ExamSolution.user_id == user_id)
        query = query.filter(ExamSolution.exam_template_id == exam_template_id)
        exam_solutions = query.all()
        logger.debug("Getting all solutions by user %s and exam template %s", user_id,exam_template_id)
        return exam_solutions

    def get_all_exam_solutions_by_corrector_id(self, db, corrector_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.corrector_id == corrector_id)
        if graded is not None:
            logger.debug("Get solutions of exam for corrector %s with filter graded %s",
                        corrector_id, graded)
            query = query.filter(ExamSolution.graded == graded)
        if approval_state is not None:
            logger.debug("Get solutions of exam for corrector %s with filter approval_state %s",
                        corrector_id, graded)
            query = query.filter(ExamSolution.approval_state == approval_state)
        exam_solutions = query.all()
        logger.debug("Getting all solutions of exam for corrector %s", corrector_id)
        return exam_solutions

    def get_all_exam_solutions_by_course_id(self, db, course_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.course_id == course_id)
        if graded is not None:
            logger.debug("Get solutions of exam for course %s with filter graded %s",
                        course_id, graded)
            query = query.filter(ExamSolution.graded == graded)
        if approval_state is not None:
            logger.debug("Get solutions of exam for course %s with filter approval_state %s",
                        course_id, graded)
            query = query.filter(ExamSolution.approval_state == approval_state)
        exam_solutions = query.all()
        logger.debug("Getting all solutions of exam for course %s", course_id)
        return exam_solutions

    def get_all_exam_solutions_by_user_id_and_course_id(self, db, user_id, course_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.user_id == user_id)
        query = query.filter(ExamSolution.course_id == course_id)
        if graded is not None:
            query = query.filter(ExamSolution.graded == graded)
        if approval_state is not None:
            query = query.filter(ExamSolution.approval_state == approval_state)
        exam_solutions = query.all()
        return exam_solutions

    def delete_exam_solution(self, db, exam_solution):
        db.delete(exam_solution)
        db.commit()
        logger.debug("Delete exam solution %s", exam_solution.id)
        logger.info("Exam solution deleted")

    def update_exam_solution(self, db):
        db.commit()
