from infrastructure.db.question_solution_schema import QuestionSolution
import logging

logger = logging.getLogger(__name__)


class QuestionSolutionRepositoryPostgres:
    def add_question_solution(self, db, question_solution):
        db.add(question_solution)
        db.commit()
        logger.info("Added new question solution")
        logger.debug("ID of the new question solution: %s", question_solution.id)

    def get_question_solution(self, db, question_solution_id):
        question_solution = db.query(QuestionSolution).filter(QuestionSolution.id == question_solution_id).first()
        logger.debug("Getting question solution %s", question_solution_id)
        return question_solution

    def get_all_question_solutions_by_question_template_id(self, db, question_template_id):
        query = db.query(QuestionSolution).filter(QuestionSolution.question_template_id == question_template_id)
        question_solutions = query.all()
        logger.debug("Getting all question solutions of question template %s", question_template_id)
        return question_solutions

    def get_all_question_solutions_by_exam_solution_id(self, db, exam_solution_id):
        query = db.query(QuestionSolution).filter(QuestionSolution.exam_solution_id == exam_solution_id)
        question_solutions = query.all()
        logger.debug("Getting all question solutions of exam solution %s", exam_solution_id)
        return question_solutions

    def delete_question_solution(self, db, question_solution):
        db.delete(question_solution)
        db.commit()
        logger.debug("Delete question solution %s", question_solution.id)
        logger.info("Question solution deleted")

    def update_question_solution(self, db):
        db.commit()
