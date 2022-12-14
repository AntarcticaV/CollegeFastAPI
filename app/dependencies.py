from app.repasitories.group import GroupTmpRepasitory
from app.repasitories.student import StudentTmpRepasitory


TMP_REPASITORY_GROUP = GroupTmpRepasitory()
TMP_REPASITORY_STUDENT = StudentTmpRepasitory()


def get_group_repo() -> GroupTmpRepasitory:
    return TMP_REPASITORY_GROUP

def get_student_repo() -> StudentTmpRepasitory:
    return TMP_REPASITORY_STUDENT