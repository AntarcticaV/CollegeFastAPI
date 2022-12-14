/*
  Warnings:

  - Made the column `group_id` on table `Student` required. This step will fail if there are existing NULL values in that column.

*/
-- DropForeignKey
ALTER TABLE "Student" DROP CONSTRAINT "Student_group_id_fkey";

-- AlterTable
ALTER TABLE "Student" ALTER COLUMN "group_id" SET NOT NULL;

-- AddForeignKey
ALTER TABLE "Student" ADD CONSTRAINT "Student_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "Group"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
