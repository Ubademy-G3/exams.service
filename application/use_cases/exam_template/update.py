from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from infrastructure.db.exam_template_schema import ExamStateEnum
from exceptions.http_exception import NotFoundException
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from exceptions.ubademy_exception import (InvalidExamStateException, InvalidExamTemplateScoreException,
                                          InvalidExamFilterException, InvalidExamTemplateAttemptsException,
                                          NonPositiveExamTemplateApprovalScoreException,
                                          HighExamTemplateApprovalScoreException)
import logging

logger = logging.getLogger(__name__)

etrp = ExamTemplateRepositoryPostgres()


def validate_flags(exam_template_to_update, new_args):

    has_multiple_choice = new_args.has_multiple_choice
    if has_multiple_choice is None:
        has_multiple_choice = exam_template_to_update.has_multiple_choice

    has_written = new_args.has_written
    if has_written is None:
        has_written = exam_template_to_update.has_written

    has_media = new_args.has_media
    if has_media is None:
        has_media = exam_template_to_update.has_media

    if(
        new_args.state is not None and
        ((has_multiple_choice is None or has_written is None or has_media is None) or
         (has_multiple_choice is False and has_written is False and has_media is False))
    ):
        raise InvalidExamFilterException(has_multiple_choice, has_written, has_media)


def get_exam_template_to_update(db, exam_template_id, new_args):

    if(new_args.state is not None and new_args.state not in ["active", "inactive"]):
        logger.warning("Invalid exam state in %s", exam_template_id)
        raise InvalidExamStateException(new_args.state)

    if(new_args.max_score is not None and new_args.max_score <= 0):
        logger.warning("Invalid exam score in %s", exam_template_id)
        raise InvalidExamTemplateScoreException(new_args.max_score)

    if new_args.approval_score is not None:
        if new_args.approval_score <= 0:
            logger.warning("Invalid exam approval score in %s", exam_template_id)
            raise NonPositiveExamTemplateApprovalScoreException(new_args.approval_score)
        if new_args.max_score is not None and new_args.approval_score > new_args.max_score:
            logger.warning("Invalid exam approval score in %s", exam_template_id)
            raise HighExamTemplateApprovalScoreException(new_args.approval_score)

    if(new_args.max_attempts is not None and new_args.max_attempts <= 0):
        logger.warning("Invalid exam approval attempts in %s", exam_template_id)
        raise InvalidExamTemplateAttemptsException(new_args.max_attempts)

    exam_template_to_update = etrp.get_exam_template(db, exam_template_id)

    if not exam_template_to_update:
        raise NotFoundException("Exam template {}".format(exam_template_id))

    if(
        new_args.approval_score is not None and new_args.max_score is None
        and new_args.approval_score > exam_template_to_update.max_score
    ):
        raise HighExamTemplateApprovalScoreException(new_args.approval_score)

    validate_flags(exam_template_to_update, new_args)

    return exam_template_to_update


def update_exam_template(db, exam_template_id, new_args):

    exam_template_to_update = get_exam_template_to_update(db, exam_template_id, new_args)

    if new_args.name is not None:
        exam_template_to_update.name = new_args.name

    if new_args.state is not None:
        exam_template_to_update.state = ExamStateEnum.active
        if(new_args.state == "inactive"):
            exam_template_to_update.state = ExamStateEnum.inactive

    if new_args.max_score is not None:
        exam_template_to_update.max_score = new_args.max_score

    if new_args.approval_score is not None:
        exam_template_to_update.approval_score = new_args.approval_score

    if new_args.has_multiple_choice is not None:
        exam_template_to_update.has_multiple_choice = new_args.has_multiple_choice

    if new_args.has_written is not None:
        exam_template_to_update.has_written = new_args.has_written

    if new_args.has_media is not None:
        exam_template_to_update.has_media = new_args.has_media

    if new_args.max_attempts is not None:
        exam_template_to_update.max_attempts = new_args.max_attempts

    logger.debug("Update exam template %s", exam_template_id)
    etrp.update_exam_template(db)
    logger.info("Exam template updated")
    return ExamTemplateSerializer.serialize(exam_template_to_update)
